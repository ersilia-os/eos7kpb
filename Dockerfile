FROM bentoml/model-server:0.11.0-py39
MAINTAINER ersilia

RUN python -m pip install --upgrade pip
RUN conda install -c conda-forge lightgbm
RUN python -m pip install streamlit
RUN python -m pip install git+https://github.com/ersilia-os/compound-embedding-lite
RUN python -m pip install flaml
RUN python -m pip install xgboost

WORKDIR /repo
COPY . /repo
