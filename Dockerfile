FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN python -m pip install --upgrade pip
RUN conda install -c conda-forge lightgbm=3.3.2
RUN python -m pip install git+https://github.com/ersilia-os/compound-embedding-lite
RUN python -m pip install flaml==2.1.2
RUN python -m pip install xgboost==2.0.3
RUN pip install numpy==1.22.4
RUN pip install pandas==2.2.1

WORKDIR /repo
COPY . /repo
