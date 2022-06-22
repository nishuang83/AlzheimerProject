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
MSphate_operator = MSphate.Multiscale_PHATE(n_pca=None)
Y_MSphate_pp = MSphate_operator.fit(data_pp)
# Y_MSphate_pp = Y_MSphate_pp.transform(visualization_level=self.algo_obj.levels[0], **opt_kwargs)

ax = plt.plot(mp_op.gradient)
ax = plt.scatter(levels, mp_op.gradient[levels], c = 'r', s=100)
######
# plot
######
ids = data_pp.obs.id
celltypes = data_pp.obs.celltype
Subclusters = data_pp.obs.Subcluster
cerad_scores = data_pp.obs.cerad_score
diagnosises = data_pp.obs.diagnosis
braak_stages = data_pp.obs.braak_stage
apoe_genotypes = data_pp.obs.apoe_genotype
fig, axes = plt.subplots(2, 3, figsize=(20, 10))
# plt.figure()
# sns.scatterplot(ax=axes[0, 0], x = tsne1, y = tsne2, hue=ids, legend=False, s = 5).set(title='ID for T-SNE')

plt.figure()
celltypes_fig = sns.scatterplot(ax=axes[0,0], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=celltypes, s = 5).set(title='Celltypes for T-SNE')
# plt.savefig(PROJECT_DIR + '/figures/tsne_celltypes_fig.pdf')

# plt.figure()
Subclusters_fig = sns.scatterplot(ax=axes[0,1], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=Subclusters, legend=False, s = 5).set(title='Subclusters for T-SNE')
# plt.savefig(PROJECT_DIR + '/figures/tsne_Subclusters_fig.pdf')

plt.figure()
cerad_scores_fig = sns.scatterplot(ax=axes[1,0], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=cerad_scores, s = 5).set(title='Cerad Score for T-SNE')
# plt.savefig(PROJECT_DIR + '/figures/tsne_ceradscore_fig.pdf')

plt.figure()
diagnosis_fig = sns.scatterplot(ax=axes[1,1], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=diagnosises, s = 5).set(title='diagnosis for T-SNE')
# plt.savefig(PROJECT_DIR + '/figures/tsne_diagnosis_fig.pdf')

plt.figure()
braak_stages_fig = sns.scatterplot(ax=axes[1,2], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=braak_stages, s = 5).set(title='braak_stages for T-SNE')
# plt.savefig(PROJECT_DIR + '/figures/tsne_braak_stages_fig.pdf')

plt.figure()
apoe_genotypes_fig = sns.scatterplot(ax=axes[0,2], x = Y_MSphate_pp[:,0], y = Y_MSphate_pp[:,1], hue=apoe_genotypes, s = 5).set(title='apoe_genotypes for T-SNE')

plt.savefig(PROJECT_DIR + '/figures/MSphate_all_fig.pdf')

