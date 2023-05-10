# imports
import os
import csv
import sys
import joblib
import collections
import pandas as pd
from eosce.models import ErsiliaCompoundEmbeddings

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# other parameters
model_names = {
    "caco": "caco_2",
    "clintH": "clint_h",
    "clintM": "clint_m",
    "clintR": "clint_r",
    "cyp_all_cyp2c9": "cyp2c9",
    "cyp_all_cyp2c19": "cyp2c19",
    "cyp_all_cyp2d6": "cyp2d6",
    "cyp_all_cyp3a4": "cyp3a4",
    "k1": "pf_k1",
    "mtb": "mtb",
    "nf54": "pf_nf54",
    "sol_65": "aq_sol_65",
    "sol": "aq_sol",
    "cho": "cho",
    "hepg2": "hepg2",
}

model_keys = [
    "nf54", "k1",
    "mtb",
    "cho",
    "hepg2",
    "clintH",
    "clintM",
    "clintR",
    "caco",
    "sol",
    "cyp_all_cyp2c9",
    "cyp_all_cyp2c19",
    "cyp_all_cyp3a4",
    "cyp_all_cyp2d6",
]

# load models function
def load_models():
    models = {}
    models_dir = os.path.join(root, "..", "..", "checkpoints", "models")
    for fn in os.listdir(models_dir):
        mn = fn.split(".joblib")[0]
        if mn in model_names:
            models[mn] = joblib.load(os.path.join(models_dir, fn))
    return models

# load scaler function
def load_precalculations():
    trf, columns = joblib.load(os.path.join(root, "..", "..", "checkpoints", "data", "precalculations_quantizer.joblib"))
    return trf, columns

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

models = load_models()
trf_precalcs, columns_precalcs = load_precalculations()
embedder = ErsiliaCompoundEmbeddings()

X = embedder.transform(smiles_list)
results = collections.OrderedDict()
results["smiles"] = smiles_list
for k in model_keys:
    if k in models:
        v = models[k]
        results[k] = list(v.predict_proba(X)[:,1])
    else:
        results[k] = [None]*X.shape[0]
data = pd.DataFrame(results)
data_precalcs = pd.DataFrame(trf_precalcs.transform(data[columns_precalcs]), columns=[model_names[x]+"_norm" for x in columns_precalcs])
data = data.rename(columns=model_names).drop(columns=["smiles"])
data = pd.concat([data, data_precalcs], axis=1)

data.to_csv(output_file, index=False)
