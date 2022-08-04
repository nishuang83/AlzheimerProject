#!/bin/bash

#SBATCH --account=rrg-bengioy-ad
#SBATCH --time=2:00:00
#SBATCH --mem=200G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --job-name=msphate2_squareroot_plot
#SBATCH --output=/home/shuangni/AlzheimerProject/job_config/job_output.txt
#SBATCH --error=/home/shuangni/AlzheimerProject/job_config/job_error.txt
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

# python /home/shuangni/AlzheimerProject/MSphate_main.py
python /home/shuangni/AlzheimerProject/plot_msphate.py
