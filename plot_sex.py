import scanpy as sc
import matplotlib.pyplot as plt
import multiscale_phate as MSphate
import pickle 
import numpy as np
import scprep
import pandas as pd

PROJECT_DIR="/home/shuangni/AlzheimerProject"
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data'


DATA_DIR_preprocessed = DATA_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_preprocessed)
data_pp.obs.diagnosis.replace({1: 1, -1:0}, inplace=True)

sex = data_pp.obs.sex

sex_list = [0.0, 1.0]

for t in range(len(sex_list)):
    if(sex_list[t] == 0.0):
        sexname = 'Female'
    else: 
        sexname = 'Male'
    #choose one celltype
    print('-----------------------Start sex: ' + sexname)
    cell_data = data_pp[sex == sex_list[t]]
    data = cell_data.to_df()

    # do MSPHATE for each sex
    mp_op =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
    levels = mp_op.fit(data)
    
    metalist = ['diagnosis', 'cerad_score', 'braak_stage', 'apoe_genotype', 'celltype']

    # plot 
    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[i+1], cluster_level = levels[-3])

        SAVE_DIR = '/home/shuangni/AlzheimerProject/figures/sex/'+ sexname + '/'
        titles = 'Multiscale_PHATE_'

        for j in range(len(metalist)):
            category = cell_data.obs[metalist[j]].values
            majority_vote, ratio = mp_op.get_majority_votes(categories = category, visualization_level = levels[i+1])
            
            plt.figure()
            scprep.plot.scatter2d(embedding, s = 50*np.sqrt(sizes), c = majority_vote, 
                      fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8), alpha = ratio)
            plt.savefig(SAVE_DIR + titles + metalist[j] +'_v_%s'%levels[i+1] +'.jpg')
            print('Saving figures for level%s with catergory '%(i) + metalist[j])