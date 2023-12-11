# Installation and Usage

## 1. Install HARL:
In terminal, run the following commands:
```
conda create -n harl python=3.8
conda activate harl
git clone https://github.com/PKU-MARL/HARL.git
cd HARL
pip install -e .
```
After that, you must install PyTorch manually via PyTorch Official Website

## 2. Install MPE:
```
pip install pettingzoo==1.22.2
pip install supersuit==3.7.0
```

## 3. Solve dependencies:
```
pip install gym==0.21.0
pip install pyglet==1.5.0
pip install importlib-metadata==4.13.0
```

## 4. How to train

### If you use yaml file: 
Modify yaml configuration files of the corresponding algorithm and environment under 
```
harl/configs/algos_cfgs
harl/configs/envs_cfgs
```
Then start training with a one-liner python command:
```python ./example/train.py --algo <ALGO> --env <ENV> --exp_name <EXPERIMENT NAME>```'

### If you want to run pretrained models:

Change the config parameter named “model_dir” in the algorithm yaml file as the path of the pre-trained model, and then run the same command as training.