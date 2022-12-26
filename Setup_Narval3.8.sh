#!/bin/bash

# Paths
PROJECT_DIR="/home/shuangni/AlzheimerProject"
ENV_LOC="/home/shuangni/AlzheimerProject/alz_env3.8"
# MSPHATE_LOC="/home/shuangni/COVIDproject/Multiscale_PHATE"
# MAGIC_LOC = '/home/shuangni/MAGIC'
module load python/3.8
# virtualenv --no-download $ENV_LOC
source $ENV_LOC/bin/activate
# pip install --no-index --upgrade pip
# pip install --no-index -r /home/shuangni/AlzheimerProject/requirements3.8.txt
# pip install -e $MSPHATE_LOC
# pip install -e $MAGIC_LOC
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"



#salloc --time=4:0:0 --account=rrg-bengioy-ad --mem=100Gb
# rm -rf $ENVDIR