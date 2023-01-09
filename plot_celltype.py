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

diagnosis = data_pp.obs.diagnosis
cerad_score = data_pp.obs.cerad_score
braak_stage = data_pp.obs.braak_stage
apoe_genotype = data_pp.obs.apoe_genotype
sex = data_pp.obs.sex
Subclusters = data_pp.obs.Subcluster


celltypes = data_pp.obs.celltype
celltype_list = ['Ast','End','Ex','In','Mic','Oli','Opc','Per']
for t in range(len(celltype_list)):
    #choose one celltype
    print('-----------------------Start celltype: ' + celltype_list[t])
    cell_data = data_pp[celltypes == celltype_list[t]]
    data = cell_data.to_df()

    # do MSPHATE for each cell type
    mp_op =  MSphate.Multiscale_PHATE(random_state=1, n_jobs=-1)
    levels = mp_op.fit(data)
    '''
    # find metadata for each celltype
    cell_diagnosis = diagnosis[celltypes.isin([celltype_list[t]])]
    metadf = pd.DataFrame(cell_diagnosis)

    cell_cerad_score = cerad_score[celltypes.isin([celltype_list[t]])]
    metadf['cerad_score'] = cell_cerad_score

    cell_braak_stage = braak_stage[celltypes.isin([celltype_list[t]])]
    metadf['braak_stage'] = cell_braak_stage

    cell_apoe_genotype = apoe_genotype[celltypes.isin([celltype_list[t]])]
    metadf['apoe_genotype'] = cell_apoe_genotype

    cell_sex = sex[celltypes.isin([celltype_list[t]])]
    metadf['sex'] = cell_sex

    cell_Subcluster = Subcluster[celltypes.isin([celltype_list[t]])]
    metadf['Subcluster'] = cell_Subcluster
    '''    
    metalist = ['diagnosis', 'cerad_score', 'braak_stage', 'apoe_genotype', 'sex', 'Subcluster']

    # plot 
    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[i+1], cluster_level = levels[-3])

        SAVE_DIR = '/home/shuangni/AlzheimerProject/figures/celltypes/'+ celltype_list[t] + '/'
        titles = 'Multiscale_PHATE_'

        for j in range(len(metalist)):
            category = cell_data.obs[metalist[j]].values
            majority_vote, ratio = mp_op.get_majority_votes(categories = category, visualization_level = levels[i+1])
            
            plt.figure()
            scprep.plot.scatter2d(embedding, s = 50*np.sqrt(sizes), c = majority_vote, 
                      fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8), alpha = ratio)
            plt.savefig(SAVE_DIR + titles + metalist[j] +'_v_%s'%levels[i+1] +'.jpg')
            print('Saving figures for level%s with catergory '%(i) + metalist[j])
