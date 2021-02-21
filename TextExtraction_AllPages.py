import cv2 as cv
import numpy as np
import pandas as pd
import os
import io
import time
import pytesseract
import PyPDF2
from wand.image import Image
from wand.color import Color

from TextExtraction_page1 import page1
from TextExtraction_page2 import page2
from TextExtraction_page3 import page3
from TextExtraction_page4 import page4_Q1, page4_Q2
from TextExtraction_page5 import page5
from TextExtraction_WriteJson import write_json
from TextExtraction_WriteCsv import write_csv

start_time = time.time()
print('--------------- Start scanning ---------------')

# Directory for all files and folders, specified by user
script_path = os.path.dirname(os.path.abspath(__file__))

#pytesseract.pytesseract.tesseract_cmd = os.path.join(script_path, 'Tesseract-OCR', 'tesseract')


# Function for creating a directory. Equivalent to using mkdir -p on the command line
def mkdir_p(mypath):
    from errno import EEXIST

    try:
        os.makedirs(mypath)
    except OSError as exc:  # Python >2.5
        if exc.errno == EEXIST and os.path.isdir(mypath):
            pass
        else:
            raise


# Function for Gamma Correction
def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv.LUT(image, table)


# Set Gamma value for Gamma Correction. Can change the value here to get different result
gamma = 0.07

# Read text csv file, need to be placed in user-specified folder
textData = pd.read_csv(os.path.join(script_path, 'configFile', <FORM_OPTION_TEXT_FILENAME>))

# Create new directory and file paths
input_dir = os.path.join(script_path, 'inputs')
user_dir = os.path.join(script_path, 'userPolicyNums')
mkdir_p(user_dir)
output_dir = os.path.join(script_path, 'outputs')
mkdir_p(output_dir)

# Store each page as tiff file
userDict = {}
for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        pdfFileObject = open(os.path.join(input_dir, filename), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

        num_of_pages = pdfReader.numPages
        policy_num = filename.replace('_', ' ').replace('.', ' ').split(' ')[-2]
        each_user_dir = os.path.join(user_dir, policy_num)
        mkdir_p(each_user_dir)
        userDict[each_user_dir] = num_of_pages  # Store 'key = directory' and 'value = number of pages' for each user

        pageList = ["page%d.tiff" % (x + 1) for x in range(num_of_pages)]

        for i in range(num_of_pages):
            page = pdfReader.getPage(i)

            dst_pdf = PyPDF2.PdfFileWriter()
            dst_pdf.addPage(page)

            pdf_bytes = io.BytesIO()
            dst_pdf.write(pdf_bytes)
            pdf_bytes.seek(0)

            with Image(file=pdf_bytes, resolution=500) as img:
                img.format = 'tiff'
                img.background_color = Color('white')
                img.alpha_channel = 'remove'
                img.save(filename=os.path.join(each_user_dir, pageList[i]))
        continue
    else:
        continue

# Read input images, convert to grayscale, apply Gamma Correction, then store in a list
imgDict = {}
imgList = []
for key, value in userDict.items():
    for page in range(value):
        path = os.path.join(key, 'page%d.tiff' % (page + 1))
        img_rgb = cv.imread(path)
        if img_rgb is not None:
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            img_adjust = adjust_gamma(img_gray, gamma=gamma)
            imgList.append(img_adjust)
    imgDict[key] = imgList  # Store 'key = directory' and 'value = list of input images' for each user


# Detect page number
def detect_page_num(image):
    # Read page number in this page as input image
    w = 200
    h = 80
    img_box = image[5355:5355+h, 3555:3555+w]

    pageNum = pytesseract.image_to_string(img_box, config='--psm 6')
    return pageNum


# Scan each page for each user and get required answers
# answerList[i][j]: i -> Index of page; j -> Index of answer as the order in each page script
answerList = []
answerPage1 = [0] * 5
answerPage2 = [0] * 5
answerPage3 = [0] * 3
answerPage4_Q1 = [0] * 20
answerPage4_Q2 = [0] * 20
answerPage5 = [0] * 10
for key, value in imgDict.items():
    policy_num = key.split('/')[-1]
    print('Number of pages for user', policy_num, ':', len(value))
    for page in range(len(value)):
        pageNum = detect_page_num(value[page])
        #print(pageNum)
        if pageNum == 'Page 1':
            print('Scanning Page 1...')
            answerPage1 = page1(value[page], textData)
            answerList.append(answerPage1)
        elif pageNum == 'Page 2':
            print('Scanning Page 2...')
            answerPage2 = page2(value[page], textData)
            answerList.append(answerPage2)
        elif pageNum == 'Page 3':
            print('Scanning Page 3...')
            answerPage3 = page3(value[page], textData)
            answerList.append(answerPage3)
        elif pageNum == 'Page 4':
            print('Scanning Page 4...')
            answerPage4_Q1 = page4_Q1(value[page], textData)
            answerPage4_Q2 = page4_Q2(value[page], textData)
            answerList.append(answerPage4_Q1+answerPage4_Q2)
        elif pageNum == 'Page 5':
            print('Scanning Page 5...')
            answerPage5 = page5(value[page], textData)
            answerList.append(answerPage5)
        elif pageNum == 'Page 6':
            print('Page 6 is blank')
        else:
            print('Number of pages is out of range')
    write_json(answerList, output_dir, policy_num)
    write_csv(answerList, output_dir, policy_num)
    print('Output for user', policy_num, 'has been generated')
print('----------------------------------------------')
print('All outputs have been generated successfully!!')
print('Execution time: %s seconds' % (time.time() - start_time))
print('----------------------------------------------')
