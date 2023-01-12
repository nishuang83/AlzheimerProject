import scanpy as sc
import matplotlib.pyplot as plt
import multiscale_phate as MSphate
import pickle 
import numpy as np
import scprep
import pandas as pd
from utils import calculate_MELD


PROJECT_DIR='/home/shuangni/AlzheimerProject'
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data'


DATA_DIR_preprocessed = DATA_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_preprocessed)
data_pp.obs.diagnosis.replace({1: 1, -1:0}, inplace=True)

# jitter plot for metadata
'''
metalist = ['sex', 'cerad_score', 'braak_stage', 'apoe_genotype', 'diagnosis']

for t in range(len(metalist)):
    name = metalist[t]
    SAVE_DIR = PROJECT_DIR + '/figures/jitter/'+ name + '_subcluster_jitter.jpg'
    labels = data_pp.obs.Subcluster
    values = data_pp.obs[metalist[t]].values
    
    plt.figure()
    scprep.plot.jitter(labels, values, c=labels, title=name, figsize=(40, 4), legend=False)
    plt.savefig(SAVE_DIR)
'''

######
# MELD
######
diagnosis_likelihoods = calculate_MELD(data_pp, data_pp.obs["diagnosis"])

pickle_diagnosis_likelihoods= open(DATA_DIR + '/data/MELD_diagnosis_likelihoods.pkl', 'wb')
pickle.dump(diagnosis_likelihoods, pickle_diagnosis_likelihoods)
pickle_diagnosis_likelihoods.close()
# jitter plot for meld diagnosis with Subcluster
labels = data_pp.obs.Subcluster
values = diagnosis_likelihoods[1]
SAVE_DIR = PROJECT_DIR + '/figures/jitter/'+ 'meld_diagnosis' + '_subcluster_jitter.jpg'
plt.figure()
scprep.plot.jitter(labels, values, c=values, title='MELD diagnosis', figsize=(40, 4), legend=False)
plt.savefig(SAVE_DIR)

# jitter plot for meld diagnosis with celltype
labels = data_pp.obs.celltype
values = diagnosis_likelihoods[1]
SAVE_DIR = PROJECT_DIR + '/figures/jitter/'+ 'meld_diagnosis' + '_jitter.jpg'
plt.figure()
scprep.plot.jitter(labels, values, c=values, title='MELD diagnosis', legend=False)
plt.savefig(SAVE_DIR)
