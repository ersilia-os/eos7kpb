FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia
RUN python -m pip install pandas==2.0.3
RUN python -m pip install scikit-learn==1.2.2
RUN python -m pip install xgboost==1.6.1 
RUN python -m pip install flaml==2.1.2
RUN python -m pip install lightgbm==3.3.2
RUN python -m pip install eosce==0.2.0
RUN python -m pip install numpy==1.26.4
WORKDIR /repo
COPY . /repo
