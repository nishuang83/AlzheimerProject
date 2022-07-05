import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate
import pickle 

PROJECT_DIR="/home/shuangni/AlzheimerProject"

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)

file = open(PROJECT_DIR + '/results/'+'msphate_operator.pkl','rb')
mp_op = pickle.load(file)  
embedding, clusters, sizes = mp_op.transform(visualization_level = 14)

######
# pickle the embedding
######
pickle_embedding = open(PROJECT_DIR + '/results/'+'embedding.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(embedding, pickle_embedding)

pickle_embedding.close()

######
# plot
######
celltypes = data_pp.obs.celltype
Subclusters = data_pp.obs.Subcluster
cerad_scores = data_pp.obs.cerad_score
diagnosises = data_pp.obs.diagnosis
braak_stages = data_pp.obs.braak_stage
apoe_genotypes = data_pp.obs.apoe_genotype
hue_list = [celltypes, Subclusters, diagnosises, cerad_scores, braak_stages, apoe_genotypes]

x_axis=embedding[:, 0]
y_axis=embedding[:, 1]
titles = 'Multiscale PHATE (preprocessed)'
plt.figure()
fig, axes = plt.subplots(2, 3, figsize=(20, 10))

sns.scatterplot(ax=axes[0,0], x = x_axis, y = y_axis, hue=hue_list[0], s = 5).set(title='Celltypes for '+ titles)

sns.scatterplot(ax=axes[0,1], x = x_axis, y = y_axis, hue=hue_list[1], legend=False, s = 5).set(title='Subclusters for '+ titles)

sns.scatterplot(ax=axes[0,2], x = x_axis, y = y_axis, hue=hue_list[2], s = 5).set(title='diagnosis for '+ titles)

sns.scatterplot(ax=axes[1,0], x = x_axis, y = y_axis, hue=hue_list[3], s = 5).set(title='Cerad Scorefor '+ titles)

sns.scatterplot(ax=axes[1,1], x = x_axis, y = y_axis, hue=hue_list[4], s = 5).set(title='braak_stages for '+ titles)

sns.scatterplot(ax=axes[1,2], x = x_axis, y = y_axis, hue=hue_list[5], s = 5).set(title='apoe_genotypes for '+ titles)

plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig.pdf')
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig.jpg')