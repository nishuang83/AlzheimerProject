import matplotlib.pyplot as plt
import multiscale_phate as MSphate
import scprep
import numpy as np

def plot_all_levels(data, titles = 'Multiscale_PHATE', levels = [], mp_op = None, PROJECT_DIR="/home/shuangni/AlzheimerProject"): 
    if levels==[] or mp_op==None:
            return print('Error: Insufficient input for ploting figures.')
    metadata = ['celltype', 'diagnosis', 'cerad_score', 'braak_stage', 'apoe_genotype']
    
    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[i+1], cluster_level = levels[-3])
        for j in range(len(metadata)):
            category = data.obs[metadata[j]].values
            
            majority_vote, ratio = mp_op.get_majority_votes(categories = category, visualization_level = levels[i+1])

            plt.figure()
            scprep.plot.scatter2d(embedding, s = 50*np.sqrt(sizes), c = majority_vote, 
                      fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8), alpha = ratio)
            plt.savefig(PROJECT_DIR + '/figures/MAGIC/'+ titles + metadata[j] +'_v_%s'%levels[i+1] +'.jpg')
            print('Saving figures for level%s with catergory'%(i) + metadata[j])

def plot_all_cluster_level(titles = 'Multiscale_PHATE', levels = [], mp_op = None, PROJECT_DIR="/home/shuangni/AlzheimerProject", vl = 1): 
    if levels==[] or mp_op==None:
            return print('Error: Insufficient input for ploting figures.')
    
    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[vl], cluster_level = levels[i+1])
        
        plt.figure()
        scprep.plot.scatter2d(embedding, s = 50*np.sqrt(sizes), c = clusters, 
                    fontsize=16, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
        plt.savefig(PROJECT_DIR + '/figures/zoomin/'+ titles +'_v3_c%s'%levels[i+1] +'.jpg')
        print('Saving figures for cluster level%s '%(i+1) )

def plot_all_levels_zoomin(titles = 'Multiscale PHATE', levels = [], mp_op = None, PROJECT_DIR="/home/shuangni/AlzheimerProject"):
    if levels==[] or mp_op==None:
            return print('Error: Insufficient input for ploting figures.')

    for i in range(len(levels)-1): 
        embedding, clusters, sizes = mp_op.transform(visualization_level = levels[i+1], cluster_level = levels[-4], coarse_cluster_level = levels[1],  coarse_cluster = 1)

        plt.figure()
        scprep.plot.scatter2d(embedding, s = 5*np.sqrt(sizes), c = clusters, fontsize=12, ticks=False,label_prefix="Multiscale PHATE", figsize=(10,8))
        plt.savefig(PROJECT_DIR + '/figures/zoom_in/'+'coarse3_cluster-4_Visuallevel_%s'%levels[i+1] +'.jpg')
        plt.close()
        print('Saving figures for level%s'%(i+1))
'''
# import meld
def calculate_MELD(data, sample_labels):
    # Estimate density of each sample over the graph
    meld_op = meld.MELD(solver='exact')
   sample_densities = meld_op.fit_transform(data, sample_labels)

   # Normalize densities to calculate sample likelihoods
   sample_likelihoods = meld.utils.normalize_densities(sample_densities)
   return sample_likelihoods
'''
if __name__ == "__main__":
    plot_all_levels()

