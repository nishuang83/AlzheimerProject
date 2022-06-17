#!/bin/bash

# Paths
PROJECT_DIR="/home/shuangni/AlzheimerProject"
ENV_LOC="/home/shuangni/AlzheimerProject/alz_env"
MSPHATE_LOC="/home/shuangni/COVIDproject/Multiscale_PHATE"

module load python/3.7
# virtualenv --no-download $ENV_LOC
source $ENV_LOC/bin/activate
pip install --no-index --upgrade pip
pip install --no-index -r /home/shuangni/AlzheimerProject/requirements.txt
pip install -e $MSPHATE_LOC
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"
#salloc --time=1:0:0 --account=rrg-bengioy-ad --mem=5Gb
# rm -rf $ENVDIR