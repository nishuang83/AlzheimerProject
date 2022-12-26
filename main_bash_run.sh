#!/bin/bash

#SBATCH --account=rrg-bengioy-ad
#SBATCH --time=1:59:00
#SBATCH --mem=500G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --job-name=msphate_magic
#SBATCH --output=/home/shuangni/AlzheimerProject/job_config/job_output.txt
#SBATCH --error=/home/shuangni/AlzheimerProject/job_config/job_error.txt
#SBATCH --mail-user=shuang.ni@mila.quebec
#SBATCH --mail-type=ALL

# path
PROJECT_DIR="/home/shuangni/AlzheimerProject"
ENV_LOC="/home/shuangni/AlzheimerProject/alz_env3.8"
MSPHATE_LOC="/home/shuangni/COVIDproject/Multiscale_PHATE"
DATA_DIR = '/home/shuangni/scratch/Alzheimer_data/data'

# Activate virtual env
module load python/3.8
source $ENV_LOC/bin/activate
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

python /home/shuangni/AlzheimerProject/MSphate_main.py
#python /home/shuangni/AlzheimerProject/plot_msphate.py
