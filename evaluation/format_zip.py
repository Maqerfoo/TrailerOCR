from zipfile import *
import shutil
import os

def format_zip(gt_zip='gt.zip', subm_zip='submit.zip'):
    file_reg = [{},{}]
    source_gt = ZipFile(gt_zip, 'r')
    source_subm = ZipFile(subm_zip, 'r')
    source_gt.extractall('gt')
    source_subm.extractall('submit')
    source_gt.close()
    source_subm.close()
    gt_filelist = os.listdir('gt')
    subm_filelist = os.listdir('submit')
    for idx, file in enumerate(gt_filelist):
        if file in subm_filelist:    
            filename_gt = ("gt_img_" + str(idx+1) + ".txt")
            filename_subm = ("res_img_" + str(idx+1) + ".txt")
            file_reg[0][filename_gt] = file
            file_reg[1][filename_subm] = file
            os.rename(('gt/' + file), 'gt/' + filename_gt)
            os.rename(('submit/' + file), 'submit/' + filename_subm)
    print(file_reg[0])
    print(file_reg[1])
    os.remove(gt_zip)
    os.remove(subm_zip)
    shutil.make_archive('submit', 'zip', 'submit')
    shutil.make_archive('gt', 'zip', 'gt')
    shutil.rmtree('submit')
    shutil.rmtree('gt')
    return file_reg; 

def return_zip(file_reg, gt_zip='gt.zip', subm_zip='submit.zip'):
    source_gt = ZipFile(gt_zip, 'r')
    source_subm = ZipFile(subm_zip, 'r')
    source_gt.extractall('gt')
    source_subm.extractall('submit')
    source_gt.close()
    source_subm.close()
    for file in os.listdir('gt'):
        os.rename(('gt/' + file), 'gt/' + file_reg[0][file])
    for file in os.listdir('submit'):
        os.rename(('submit/' + file), 'submit/' + file_reg[1][file])
    os.remove(gt_zip)
    os.remove(subm_zip)
    shutil.make_archive('submit', 'zip', 'submit')
    shutil.make_archive('gt', 'zip', 'gt')
    shutil.rmtree('submit')
    shutil.rmtree('gt')


if __name__=='__main__':
    file_reg = format_zip()
    return_zip(file_reg)