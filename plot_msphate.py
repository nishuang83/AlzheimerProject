import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import multiscale_phate as MSphate
import pickle 
import scprep
import numpy as np
from utils import plot_all_levels

PROJECT_DIR="/home/shuangni/AlzheimerProject"

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)

read_levels = open(PROJECT_DIR + '/results/1st/'+'levels.pkl','rb')
levels = pickle.load(read_levels)  
print(levels)

read_operator = open(PROJECT_DIR + '/results/1st/'+'msphate_operator.pkl','rb')
mp_op = pickle.load(read_operator)  

######
# plot all
######
# plot_all_levels(levels = levels, mp_op = mp_op)

######
# plot one
######
# embedding, clusters, sizes = mp_op.transform(visualization_level = levels[2],cluster_level = levels[-2])
# titles = 'Multiscale PHATE'
# plt.figure()
# scprep.plot.scatter2d(embedding, s = 100*np.sqrt(sizes), c = clusters,
#                       fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
# plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig_level_0.jpg')

######
# plot level[2] with diagnosis_expression
######
data_pp.obs["diagnosis"].replace({"1": "1", "-1": "0"}, inplace=True)

embedding, clusters, sizes = mp_op.transform(visualization_level = levels[2],cluster_level = levels[-2])

diagnosis_expression = mp_op.get_expression(data_pp.obs.diagnosis.values, visualization_level =  levels[2])

plt.figure()
scprep.plot.scatter2d(embedding, s = 5*np.sqrt(sizes),c=diagnosis_expression,title='diagnosis',xticks=False, yticks=False, label_prefix="Multiscale PHATE", fontsize=16, cmap = 'RdBu_r')
plt.savefig(PROJECT_DIR + '/figures/Multiscale PHATE diagnosis_expression.jpg')
print('Saving figures for diagnosis_expression')