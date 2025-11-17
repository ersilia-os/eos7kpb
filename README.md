# H3D virtual screening cascade light

This panel of models provides predictions for the H3D virtual screening cascade. It leverages the Ersilia Compound Embedding and FLAML. The H3D virtual screening cascade contains models for Mycobacterium tuberculosis and Plasmodium falciparum IC50 predictions, as well as ADME, cytotoxicity and solubility assays

This model was incorporated on 2023-05-09.


## Information
### Identifiers
- **Ersilia Identifier:** `eos7kpb`
- **Slug:** `h3d-virtual-screening-cascade-light`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`, `Malaria`, `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`, `Plasmodium falciparum`, `Homo sapiens`, `Rattus norvegicus`, `Mus musculus`
- **Tags:** `Malaria`, `P.falciparum`, `Tuberculosis`, `M.tuberculosis`, `ADME`, `Cytotoxicity`, `Solubility`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `28`
- **Output Consistency:** `Fixed`
- **Interpretation:** The raw scores are the ones emerging from the FLAML model. The ones with a sufix _norm represent the percentile in the scale 0-1 over a ChEMBL dataset of 200k compounds.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pf_nf54 | float | high | Probability of inhibiting Pfalciparum NF54 strain in vitro (IC50 assay 0.1 uM cut-off) |
| pf_k1 | float | high | Probability of inhibiting Pfalciparum K1 strain in vitro (IC50 assay 0.1 uM cut-off) |
| mtb | float | high | Probability of inhibiting Mtuberculosis H37Rv strain in vitro (MIC90 assay 5 uM cut-off) |
| cho | float | high | Probability of citotoxicity measured in CHO cells (IC50 assay 10 uM cut-off) |
| hepg2 | float | high | Probability of citotoxicity measured in HepG2 cells (IC50 assay 10 uM cut-off) |
| clint_h | float | high | Probability of being cleared by human microsomes in vitro (cut-off 11.6 ug/min/mg) |
| clint_m | float | high | Probability of being cleared by mouse microsomes in vitro (cut-off 11.6 ug/min/mg) |
| clint_r | float | high | Probability of being cleared by rat microsomes in vitro (cut-off 11.6 ug/min/mg) |
| caco_2 | float | high | Probability of being permeable across membranes measured as passive permeability in Caco-2 cells (cut-off 10e-6 cm/s) |
| aq_sol | float | high | Probability of being soluble in water at pH = 7.4 (cut-off 90 um) |

_10 of 28 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7kpb](https://hub.docker.com/r/ersiliaos/eos7kpb)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7kpb.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7kpb.zip)

### Resource Consumption
- **Model Size (Mb):** `117`
- **Environment Size (Mb):** `1099`
- **Image Size (Mb):** `1348.7`

**Computational Performance (seconds):**
- 10 inputs: `37.93`
- 100 inputs: `28.13`
- 10000 inputs: `657.74`

### References
- **Source Code**: [https://github.com/ersilia-os/h3d-screening-cascade-models](https://github.com/ersilia-os/h3d-screening-cascade-models)
- **Publication**: [https://www.nature.com/articles/s41467-023-41512-2](https://www.nature.com/articles/s41467-023-41512-2)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7kpb
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7kpb
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
