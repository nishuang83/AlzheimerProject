import scanpy as sc
import pandas as pd
# import numpy as np
# import sklearn
# import phate
import matplotlib.pyplot as plt
 
PROJECT_DIR = "/home/shuangni/AlzheimerProject"
# DATA_DIR_raw = PROJECT_DIR + '/data/msPHATE_data_raw.h5ad'
# data_raw = sc.read_h5ad(DATA_DIR_raw)
# print(data_raw)
# AnnData object with n_obs × n_vars = 82159 × 32738
# obs: 'id', 'amyloid', 'plaq_n', 'nft', 'tangles', 'cogn_global_lv', 'gpath', 'gpath_3neocort', 'amyloid.group', 'caa_4gp', 'ceradsc', 'braaksc', 'niareagansc', 'cogdx', 'msex', 'pathology.group', 'diagnosis'
# var: 'gene_id'

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)
print(data_pp.obs.tsne1)
# AnnData object with n_obs × n_vars = 70634 × 17926
# obs: 'id', 'tsne1', 'tsne2', 'pre.cluster', 'celltype', 'Subcluster', 'apoe_genotype', 'braak_stage', 'cerad_score', 'age_death', 'sex', 'pmi', 'concensus_diagnosis', 'diagnosis_cerad', 'diagnosis', 'n_genes_by_counts', 
# 'total_counts'
# var: 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'

######
# tsne results
######
tsne1 = data_pp.obs.tsne1
tsne2 = data_pp.obs.tsne2

plt.scatter(tsne1, tsne2)
plt.show()