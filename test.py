import scanpy as sc
import anndata
import pandas as pd

PROJECT_DIR = "/home/shuangni/AlzheimerProejct"
DATA_DIR = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'

data = anndata.read(DATA_DIR)