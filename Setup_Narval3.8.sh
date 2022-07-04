#!/bin/bash

# Paths
PROJECT_DIR="/home/shuangni/AlzheimerProject"
ENV_LOC="/home/shuangni/AlzheimerProject/alz_env3.8"
MSPHATE_LOC="/home/shuangni/COVIDproject/Multiscale_PHATE"

module load python/3.8
# virtualenv --no-download $ENV_LOC
source $ENV_LOC/bin/activate
# pip install --no-index --upgrade pip
# pip install --no-index -r /home/shuangni/AlzheimerProject/requirements3.8.txt
# pip install -e $MSPHATE_LOC
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"



#salloc --time=2:0:0 --account=rrg-bengioy-ad --mem=50Gb
# rm -rf $ENVDIR