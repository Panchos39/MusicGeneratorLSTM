#!/bin/bash
export PATH="/usr/local/anaconda3-5.0.0/bin:$PATH"
conda create -p /tmp/reinforce -n reinforce python=3.7
source activate reinforce
cat req.txt | xargs -n 1 pip install
python -m ipykernel install --user --name reinforce
jupyter-notebook --ip=0.0.0.0 --port=8080
