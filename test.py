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

with open('embedding.txt','w') as f:
    f.writelines(embedding)



