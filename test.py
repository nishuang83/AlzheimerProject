import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate

PROJECT_DIR="/home/shuangni/AlzheimerProject"
# DATA_DIR_raw = PROJECT_DIR + '/data/msPHATE_data_raw.h5ad'
# data_raw = sc.read_h5ad(DATA_DIR_raw)

DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
data_pp = sc.read(DATA_DIR_pp)

######
# PHATE
######
# phate_operator = phate.PHATE(n_jobs=-2)
# Y_MSphate_pp = phate_operator.fit_transform(data_pp)

######
# MSphate
######
# MSphate_operator = MSphate.Multiscale_PHATE(n_pca=None)
# Y_MSphate_pp = MSphate_operator.fit(data_pp)
# Y_MSphate_pp = Y_MSphate_pp.transform(visualization_level=self.algo_obj.levels[0], **opt_kwargs)

# MSphate_operator =  MSphate.Multiscale_PHATE(random_state=1)
# levels = MSphate_operator.fit(data_raw)

######
# MSphate for data_pp
######
mp_op =  MSphate.Multiscale_PHATE(random_state=1)
levels = mp_op.fit(data_pp)

plt.figure()
plt.plot(mp_op.gradient)
plt.scatter(levels, mp_op.gradient[levels], c = 'r', s=100)
plt.savefig(PROJECT_DIR + '/results/'+'levels.jpg')
print(levels)
embedding, clusters, sizes = mp_op.transform(visualization_level = levels[2],cluster_level = levels[1])

with open(PROJECT_DIR + '/results/'+'embedding.txt','w') as f:
    f.writelines(embedding)

# plot
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

fig, axes = plt.subplots(2, 3, figsize=(20, 10))

sns.scatterplot(ax=axes[0,0], x = x_axis, y = y_axis, hue=hue_list[0], s = 5).set(title='Celltypes for '+ titles)

sns.scatterplot(ax=axes[0,1], x = x_axis, y = y_axis, hue=hue_list[1], legend=False, s = 5).set(title='Subclusters for '+ titles)

sns.scatterplot(ax=axes[0,2], x = x_axis, y = y_axis, hue=hue_list[2], s = 5).set(title='diagnosis for '+ titles)

sns.scatterplot(ax=axes[1,0], x = x_axis, y = y_axis, hue=hue_list[3], s = 5).set(title='Cerad Scorefor '+ titles)

sns.scatterplot(ax=axes[1,1], x = x_axis, y = y_axis, hue=hue_list[4], s = 5).set(title='braak_stages for '+ titles)

sns.scatterplot(ax=axes[1,2], x = x_axis, y = y_axis, hue=hue_list[5], s = 5).set(title='apoe_genotypes for '+ titles)

plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig.pdf')
plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig.jpg')






