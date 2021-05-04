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
pip install gdown
pip install fvcore-master.zip
python setup.py build develop
cd out_dir_r101
if [ -d "/out_dir_r101/icdar2015_model" ] 
then
    cd out_dir_r101/icdar2015_model 
else
    cd out_dir_r101
    mkdir icdar2015_model
    cd icdar2015_model
fi;
gdown https://drive.google.com/uc?id=18Ll-3bAmi4CR2eGTuM-j6fkMrSAaBV4Z
