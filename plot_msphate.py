import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import multiscale_phate as MSphate
import pickle 
import scprep
import numpy as np
from utils import plot_all_levels, plot_all_cluster_level

PROJECT_DIR="/home/shuangni/AlzheimerProject"
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data/data/'

DATA_DIR_preprocessed = DATA_DIR + 'msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_preprocessed)
data_pp.obs.diagnosis.replace({1: 1, -1:0}, inplace=True)

read_levels = open(PROJECT_DIR + '/results/1st/'+'levels.pkl','rb')
levels = pickle.load(read_levels)  
print(levels)

read_operator = open(PROJECT_DIR + '/results/1st/'+'msphate_operator.pkl','rb')
mp_op = pickle.load(read_operator)  
print("operator loaded")

# print levels
'''
plt.figure()
plt.plot(mp_op.gradient)
plt.scatter(levels, mp_op.gradient[levels], c = 'r', s=100)
plt.xlabel('Level')
plt.ylabel('Gradient')
plt.yticks([])
plt.savefig(PROJECT_DIR + '/results/1st/'+'levels_magic.jpg')
print('levels = ',levels)
'''
######
# plot all with catagory
######
# plot_all_levels(data = data_pp, levels = levels, mp_op = mp_op)

######
# plot all with different cluster level , vl: visulization level
######
plot_all_cluster_level(levels = levels, mp_op = mp_op, vl = 3)

######
# plot one
######
'''
embedding, clusters, sizes = mp_op.transform(visualization_level = levels[2],cluster_level = levels[2])
majority_vote, ratio = mp_op.get_majority_votes(categories = data_pp.obs["diagnosis"].values, visualization_level = levels[2])
titles = 'Multiscale PHATE'
plt.figure()
scprep.plot.scatter2d(embedding, s = 100*np.sqrt(sizes), c = majority_vote,
                      fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8), alpha = ratio)
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_v2_diagnosis.jpg')




'''
# MELD
# data_pp.obs["diagnosis"].replace({1: 1, -1: 0}, inplace=True)
# diagnosis_likelihoods = calculate_MELD(data_pp, data_pp.obs["diagnosis"])
# diagnosis_expression = mp_op.get_expression(diagnosis_likelihoods[1], visualization_level =  levels[2])

# plt.figure()
# scprep.plot.scatter2d(embedding, s = 5*np.sqrt(sizes),c=diagnosis_expression,title='diagnosis',xticks=False, yticks=False, label_prefix="Multiscale PHATE", fontsize=16, cmap = 'RdBu_r')
# plt.savefig(PROJECT_DIR + '/figures/squareroot/Multiscale PHATE diagnosis_expression_exact.jpg')
# print('Saving figures for diagnosis_expression_revised')