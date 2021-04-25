ENVS=$(conda env list | awk '{print $1}' )
if [[ $ENVS = *"textfusenet"* ]]; then
   conda activate textfusenet
else 
   conda create --name textfusenet python=3.7.3
   conda activate textfusenet
   conda install pytorch=1.3.1 torchvision cudatoolkit=10.1 -c pytorch
   pip install opencv-python
   pip install tensorboard
   pip install yacs
   pip install tqdm
   pip install termcolor
   pip install tabulate
   pip install matplotlib
   pip install cloudpickle
   pip install wheel
   pip install pycocotools
   exit
fi;
pip install fvcore-master.zip
python setup.py build develop