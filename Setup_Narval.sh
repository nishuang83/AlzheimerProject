#!/bin/bash

# Paths
ENV_LOC="/home/shuangni/AlzheimerProejct/Alz_env"

PROJECT_DIR="/home/shuangni/AlzheimerProejct"

module load python/3.7
#virtualenv --no-download $ENV_LOC
source $ENV_LOC/bin/activate
pip install --no-index --upgrade pip

#salloc --time=2:0:0 --account=rrg-bengioy-ad