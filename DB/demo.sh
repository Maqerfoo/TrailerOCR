for f in IVtext/*.jpg;
do
    python demo.py experiments/seg_detector/ic15_resnet18_deform_thre.yaml --image_path $f --resume model/ic15_resnet18 --box_thresh 0.7 --visualize
done