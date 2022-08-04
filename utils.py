
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import phate
import multiscale_phate as MSphate
import pickle 
import scprep
import numpy as np
import meld


def plot_all_levels(titles = 'Multiscale PHATE', levels = [], mp_op = None, PROJECT_DIR="/home/shuangni/AlzheimerProject"): 
    if levels==[] or mp_op==None:
            return print('Error: Insufficient input for ploting figures.')

    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[i+1], cluster_level = levels[-3])

        plt.figure()
        scprep.plot.scatter2d(embedding, s = 100*np.sqrt(sizes), c = clusters, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
        plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig_cluster-3_Visuallevel_%s'%levels[i+1] +'.jpg')
        print('Saving figures for level%s'%(i+1))

    # embedding, clusters, sizes = mp_op.transform(visualization_level = levels[0], cluster_level = levels[-2])
    # plt.figure()
    # scprep.plot.scatter2d(embedding, s = 1*np.sqrt(sizes), c = clusters, fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
    # plt.savefig(PROJECT_DIR + '/figures/'+ titles +'_all_fig_cluster132_Visuallevel_%s'%levels[0] +'.jpg')
    # print('Saving figures for level%s'%(0))

def calculate_MELD(data, sample_labels):
    # Estimate density of each sample over the graph
   sample_densities = meld.MELD().fit_transform(data, sample_labels)

   # Normalize densities to calculate sample likelihoods
   sample_likelihoods = meld.utils.normalize_densities(sample_densities)
   return sample_likelihoods

if __name__ == "__main__":
    plot_all_levels()

