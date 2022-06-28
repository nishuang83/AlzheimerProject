#!/bin/bash

#SBATCH --account=rrg-bengioy-ad
#SBATCH --time=7:00:00
#SBATCH --mem=50G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --job-name=msphate
#SBATCH --output=experiment/slurm_output/R-%x.%j.out
#SBATCH --error=experiment/slurm_output/R-%x.%j.err
#SBATCH --mail-user=shuang.ni@mila.quebec
#SBATCH --mail-type=ALL

# path
PROJECT_DIR="/home/shuangni/AlzheimerProject"
ENV_LOC="/home/shuangni/AlzheimerProject/alz_env3.8"
MSPHATE_LOC="/home/shuangni/COVIDproject/Multiscale_PHATE"

# Activate virtual env
module load python/3.8
source $ENV_LOC/bin/activate
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

python /home/shuangni/AlzheimerProject/test.py