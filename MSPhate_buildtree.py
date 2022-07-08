import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate
import pickle 
import scprep
import numpy as np

PROJECT_DIR="/home/shuangni/AlzheimerProject"

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)
data_input = data_pp.to_df() #convert to pandas dataframe

read_levels = open(PROJECT_DIR + '/results/'+'levels.pkl','rb')
levels = pickle.load(read_levels)  
print(levels)

read_operator = open(PROJECT_DIR + '/results/'+'msphate_operator.pkl','rb')
mp_op = pickle.load(read_operator)

######
# MSphate build tree
######
# NxTs : list of lists
#         Cluster assignment for every point at all levels of Diffusion
#         Condensation tree
# Xs : list of 2D numpy arrays
#         List of condensed diffusion potentials

# knn = 200
# landmarks = 2000
# npca = 100
# NxTs, Xs, Ks, Merges, diff_op, data_pca, pca, partition_clusters, diff_pca= mp_op.build_tree(df[cols_input].values,
#                                                                                          knn=knn,
#                                                                                          landmarks=landmarks,
#                                                                                           n_pca=npca,
#                                                                                           partitions=None
#                                                                                          )
NxTs = mp_op.NxTs
Xs = mp_op.Xs
np.savetxt(PROJECT_DIR + '/results/'+'NxTs.txt', NxTs)        
print('NxTs saved')
pickle.dump(np.array(Xs), open(PROJECT_DIR + '/results/'+'Xs.pickle', 'wb'))
print('Xs saved')