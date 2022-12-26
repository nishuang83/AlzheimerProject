import scanpy as sc
#import anndata
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#import seaborn as sns
#import phate
import multiscale_phate as MSphate
import pickle 
import numpy as np
import scprep
import magic
# from utils import plot_all_levels

PROJECT_DIR="/home/shuangni/AlzheimerProject"
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data/data/'

DATA_DIR_preprocessed = DATA_DIR + 'msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_preprocessed)

# original
mp_op =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
levels = mp_op.fit(data_pp)
embedding, clusters, sizes = mp_op.transform(visualization_level = levels[-2],cluster_level = levels[-2])
plt.figure()
scprep.plot.scatter2d(embedding, s = 100*np.sqrt(sizes), c = clusters, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
titles = 'Multiscale PHATE'
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_c-2_v-2.jpg')
print('Saving figures for original')


# MAGIC
magic_op = magic.MAGIC()
emt_magic = magic_op.fit_transform(data_pp, genes='all_genes')

mp_op_magic =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
levels_magic = mp_op_magic.fit(emt_magic)
embedding_magic, clusters_magic, sizes_magic = mp_op_magic.transform(visualization_level = levels_magic[-2],cluster_level = levels_magic[-2])
plt.figure()
scprep.plot.scatter2d(embedding_magic, s = 100*np.sqrt(sizes), c = clusters, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
titles = 'Multiscale PHATE with MAGIC Imputation'
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_c-2_v-2.jpg')
print('Saving figures for MAGIC')

######
# pickle the levels
######
pickle_levels = open(PROJECT_DIR + '/results/squareroot/'+'levels.pkl', 'wb')
pickle.dump(levels, pickle_levels)
pickle_levels.close()

######
# pickle the operator
######
pickle_operator = open(PROJECT_DIR + '/results/'+'msphate_operator_magic.pkl', 'wb')
pickle.dump(mp_op_magic, pickle_operator)
pickle_operator.close()
print('operator saved')

