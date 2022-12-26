import scanpy as sc
import matplotlib.pyplot as plt
import multiscale_phate as MSphate
import pickle 
import numpy as np
import scprep
import magic
import pandas as pd
from utils import plot_all_levels

PROJECT_DIR="/home/shuangni/AlzheimerProject"
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data'


DATA_DIR_preprocessed = DATA_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_preprocessed)
data = data_pp.to_df() #convert to pandas dataframe
#data_norm, libsize = scprep.normalize.library_size_normalize(data_input, return_library_size=True)
#data_sqrt = np.sqrt(data_norm)

######
# pickle the data_sqrt
######
#pickle_data_sqrt = open(DATA_DIR+'data_sqrt.pkl', 'wb')
#pickle.dump(data_sqrt, pickle_data_sqrt)
#pickle_data_sqrt.close()
'''
######
# MSphate
######
# pick a specific level
mp_op =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
levels = mp_op.fit(data)
plt.figure()
ax = plt.plot(mp_op.gradient)
ax = plt.scatter(levels, mp_op.gradient[levels], c = 'r', s=100)
plt.savefig(PROJECT_DIR + '/results/original/'+'levels_original.jpg')
print('levels = ',levels)

# pickle the levels
pickle_levels = open(PROJECT_DIR + '/results/original/'+'levels.pkl', 'wb')
pickle.dump(levels, pickle_levels)
pickle_levels.close()

# pickle the operator
pickle_operator = open(PROJECT_DIR + '/results/original/'+'msphate_operator.pkl', 'wb')
pickle.dump(mp_op, pickle_operator)
pickle_operator.close()
print('operator saved')

######
# plot results of all levels and save
######
# plot_all_levels(levels = levels, mp_op = mp_op, PROJECT_DIR = PROJECT_DIR)

# do the MSphate transform on visualization_level = level[2], cluster_level = levels[-2]
embedding, clusters, sizes = mp_op.transform(visualization_level = levels[3],cluster_level = levels[-3])
plt.figure()
scprep.plot.scatter2d(embedding, s = 100*np.sqrt(sizes), c = clusters, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
titles = 'Multiscale PHATE'
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_v3_c-3.jpg')
print('Saving figures for MAGIC')
'''
# pickle the embedding, clusters, sizes 
'''
pickle_embedding = open(PROJECT_DIR + '/results/original/'+'embedding.pkl', 'wb')
pickle.dump(embedding, pickle_embedding)
pickle_embedding.close()
print('embedding saved')

pickle_clusters = open(PROJECT_DIR + '/results/original/'+'clusters.pkl', 'wb')
pickle.dump(clusters, pickle_clusters)
pickle_clusters.close()
print('clusters saved')

pickle_sizes = open(PROJECT_DIR + '/results/original/'+'sizes.pkl', 'wb')
pickle.dump(sizes, pickle_sizes)
pickle_sizes.close()
print('sizes saved')

######
# NxTs : list of lists: Cluster assignment for every point at all levels of Diffusion, Condensation tree
# Xs : list of 2D numpy arrays: List of condensed diffusion potentials
######
NxTs = mp_op.NxTs
Xs = mp_op.Xs
np.savetxt(PROJECT_DIR + '/results/squareroot/'+'NxTs.txt', NxTs)        
print('NxTs saved')
pickle.dump(np.array(Xs), open(PROJECT_DIR + '/results/squareroot/'+'Xs.pkl', 'wb'))
print('Xs saved')
'''

######
# MAGIC
######
#magic_op = magic.MAGIC()
#emt_magic = magic_op.fit_transform(data, genes='all_genes')

# pickle the magiclevels
#pickle_magic = open(DATA_DIR + '/results/MAGIC/'+'emt_magic.pkl', 'wb')
#pickle.dump(emt_magic, pickle_magic)
#pickle_magic.close()

read_magic = open(DATA_DIR + '/results/MAGIC/'+'emt_magic.pkl','rb')
emt_magic = pickle.load(read_magic)  

mp_op_magic =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
levels_magic = mp_op_magic.fit(emt_magic)

# pickle the levels
pickle_levels = open(DATA_DIR + '/results/MAGIC/'+'levels_magic.pkl', 'wb')
pickle.dump(levels_magic, pickle_levels)
pickle_levels.close()

# pickle the operator
pickle_operator = open(DATA_DIR + '/results/MAGIC/'+'msphate_operator_magic.pkl', 'wb')
pickle.dump(mp_op_magic, pickle_operator)
pickle_operator.close()
print('MAGIC operator saved')

'''
embedding_magic, clusters_magic, sizes_magic = mp_op_magic.transform(visualization_level = levels_magic[3],cluster_level = levels_magic[-3])
plt.figure()
scprep.plot.scatter2d(embedding_magic, s = 100*np.sqrt(sizes_magic), c = clusters_magic, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
titles = 'Multiscale PHATE with MAGIC Imputation'
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_v3_c-3.jpg')
print('Saving figures for MAGIC')
'''
# print levels
plt.figure()
plt.plot(mp_op_magic.gradient)
plt.scatter(levels_magic, mp_op_magic.gradient[levels_magic], c = 'r', s=100)
plt.xlabel('Level')
plt.ylabel('Gradient')
plt.yticks([])
plt.savefig(PROJECT_DIR + '/figures/MAGIC/'+'levels_magic.jpg')
print('levels = ',levels_magic)

plot_all_levels(data = data_pp,titles = 'Multiscale_PHATE_MAGIC', levels = levels_magic, mp_op = mp_op_magic)








