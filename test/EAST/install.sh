python3.7 -m virtualenv venv 
source venv/bin/activate
pip install -r requirements.txt
pip install gdown
mkdir tmp
cd tmp
gdown https://drive.google.com/uc?id=1hfIzGuQn-xApDYiucMDZvOCosyAVwvku
gdown https://drive.google.com/uc?id=1gnkdCToYQfdU3ssaOareFTBr0Nz6u4rr
cd ..
python eval.py --gpu_list=0 --test_data_path=../sample/ --model_path=tmp/EAST_IC15+13_model.h5 --output_dir=tmp/eval/