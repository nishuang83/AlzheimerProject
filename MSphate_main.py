import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate
import pickle 
from utils import plot_all_levels

PROJECT_DIR="/home/shuangni/AlzheimerProject"
# DATA_DIR_raw = PROJECT_DIR + '/data/msPHATE_data_raw.h5ad'
# data_raw = sc.read_h5ad(DATA_DIR_raw)

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)
data_input = data_pp.to_df() #convert to pandas dataframe

######
# MSphate
######
# pick a specific level
mp_op =  MSphate.Multiscale_PHATE(random_state=1)
levels = mp_op.fit(data_input)
plt.figure()
ax = plt.plot(mp_op.gradient)
ax = plt.scatter(levels, mp_op.gradient[levels], c = 'r', s=100)
plt.savefig(PROJECT_DIR + '/results/'+'levels.jpg')
# print('levels = ',levels)

######
# pickle the levels
######
pickle_levels = open(PROJECT_DIR + '/results/'+'levels.pkl', 'wb')
pickle.dump(levels, pickle_levels)
pickle_levels.close()

######
# pickle the operator
######
pickle_operator = open(PROJECT_DIR + '/results/'+'msphate_operator.pkl', 'wb')
pickle.dump(mp_op, pickle_operator)
pickle_operator.close()

######
# plot results of all levels and save
######
plot_all_levels(levels = levels, mp_op = mp_op, PROJECT_DIR = PROJECT_DIR)

# do the MSphate transform on visualization_level = level[2], cluster_level = levels[-2]
embedding, clusters, sizes = mp_op.transform(visualization_level = levels[2],cluster_level = levels[-2])

######
# pickle the embedding, clusters, sizes 
######
pickle_embedding = open(PROJECT_DIR + '/results/'+'embedding.pkl', 'wb')
pickle.dump(embedding, pickle_embedding)
pickle_embedding.close()
print('embedding saved')

pickle_clusters = open(PROJECT_DIR + '/results/'+'clusters_0.pkl', 'wb')
pickle.dump(clusters, pickle_clusters)
pickle_clusters.close()
print('clusters saved')

pickle_sizes = open(PROJECT_DIR + '/results/'+'sizes_0.pkl', 'wb')
pickle.dump(sizes, pickle_sizes)
pickle_sizes.close()
print('sizes saved')

######
# NxTs : list of lists: Cluster assignment for every point at all levels of Diffusion, Condensation tree
# Xs : list of 2D numpy arrays: List of condensed diffusion potentials
######
NxTs = mp_op.NxTs
Xs = mp_op.Xs
np.savetxt(PROJECT_DIR + '/results/'+'NxTs.txt', NxTs)        
print('NxTs saved')
pickle.dump(np.array(Xs), open(PROJECT_DIR + '/results/'+'Xs.pickle', 'wb'))
print('Xs saved')









