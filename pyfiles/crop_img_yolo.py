import xml.etree.ElementTree as ET
import os
import ntpath
from glob import glob
import cv2
from collections import defaultdict
import pickle
import os.path, time
import shutil
dictxml = defaultdict(int)
folder_list = defaultdict(int)
index = 0
if not os.path.exists('Cropped_Images'):
    os.mkdir('Cropped_Images')
    
def xml_to_crop(f):
    global index 
    name1 = os.path.splitext(ntpath.basename(f))[0]
    img_name = f'images/{name1}.jpg'
    print("same",f)
    xmlTree = ET.parse(f)
    rootElement = xmlTree.getroot()
    for member in rootElement.findall('object'):
        yolo_id = member[5].text
        folder_name = f'Cropped_Images/{member[0].text}'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            folder_list[folder_name]
        img = cv2.imread(img_name,cv2.IMREAD_COLOR)
        crop_img = img[int(member[4][1].text):int(member[4][3].text),int(member[4][0].text):int(member[4][2].text)]
        try:
            status = cv2.imwrite(os.path.join(folder_name , f'{name1}-{yolo_id}.jpg'), crop_img)
        except:
             pass
    index = index + 1
    print('process',index)    
    
if __name__ == "__main__":
        for file in glob(os.path.join('annotation', '*.xml')):
            xml_to_crop(file)    
            






