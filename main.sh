
for file in /images/*
do
    # 1)find text
    # 2)extract coordinates
    python image_correction.py --image $file --coords "[(63, 242), (291, 110), (361, 252), (78, 386)]"
    # 3)correct the skew ^
    # 4)greyscale + binarization
    # 5)OCR engine, read text
done