import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate

PROJECT_DIR="/home/shuangni/AlzheimerProject"
DATA_DIR_raw = PROJECT_DIR + '/data/msPHATE_data_raw.h5ad'
data_raw = sc.read_h5ad(DATA_DIR_raw)

# DATA_DIR_pp = PROJECT_DIR + '/data/msPHATE_data_pp.h5ad'
# data_pp = sc.read(DATA_DIR_pp)

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

#raw data
MSphate_operator =  MSphate.Multiscale_PHATE(random_state=1)
levels = MSphate_operator.fit(data_raw)

ax = plt.plot(MSphate_operator.gradient)
ax = plt.scatter(levels, MSphate_operator.gradient[levels], c = 'r', s=100)
plt.show()
print(levels)
######
# plot
######
# ids = data_pp.obs.id
# celltypes = data_pp.obs.celltype
# Subclusters = data_pp.obs.Subcluster
# cerad_scores = data_pp.obs.cerad_score
# diagnosises = data_pp.obs.diagnosis
# braak_stages = data_pp.obs.braak_stage
# apoe_genotypes = data_pp.obs.apoe_genotype


