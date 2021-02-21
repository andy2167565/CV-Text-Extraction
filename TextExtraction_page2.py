import cv2 as cv
import os
from operator import itemgetter
import pytesseract

# Directory for tesseract
script_path = os.path.dirname(os.path.abspath(__file__))
#pytesseract.pytesseract.tesseract_cmd = os.path.join(script_path, 'Tesseract-OCR', 'tesseract')


def page2(img_gray, textData):
    # Read all boxes in this page as input images for comparison
    # Left margin: 1~1.1 cm
    # Upper margin: 1~1.1 cm
    w = 80
    h = 80
    # Q3
    img_box1 = img_gray[615:615+h, 309:309+w]
    img_box2 = img_gray[720:720+h, 309:309+w]
    img_box3 = img_gray[825:825+h, 309:309+w]
    img_box4 = img_gray[930:930+h, 309:309+w]
    img_box5 = img_gray[1033:1033+h, 309:309+w]
    img_box6 = img_gray[1138:1138+h, 309:309+w]
    img_box7 = img_gray[615:615+h, 2068:2068+w]
    img_box8 = img_gray[720:720+h, 2068:2068+w]
    img_box9 = img_gray[824:824+h, 2068:2068+w]
    img_box10 = img_gray[929:929+h, 2068:2068+w]
    img_box11 = img_gray[1033:1033+h, 2068:2068+w]
    img_box12 = img_gray[1138:1138+h, 2068:2068+w]
    # Q4
    img_box13 = img_gray[1795:1795+h, 312:312+w]
    img_box14 = img_gray[1795:1795+h, 1184:1184+w]
    # Q4_a
    img_box15 = img_gray[2092:2092+h, 449:449+w]
    img_box16 = img_gray[2092:2092+h, 2070:2070+w]
    img_box17 = img_gray[2196:2196+h, 449:449+w]
    img_box18 = img_gray[2196:2196+h, 2070:2070+w]
    img_box19 = img_gray[2301:2301+h, 517:517+w]
    img_box20 = img_gray[2405:2405+h, 517:517+w]
    img_box21 = img_gray[2510:2510+h, 517:517+w]
    img_box22 = img_gray[2614:2614+h, 517:517+w]
    img_box23 = img_gray[2719:2719+h, 517:517+w]
    img_box24 = img_gray[2301:2301+h, 2070:2070+w]
    img_box25 = img_gray[2405:2405+h, 2070:2070+w]
    img_box26 = img_gray[2510:2510+h, 2070:2070+w]
    img_box27 = img_gray[2614:2614+h, 2070:2070+w]
    img_box28 = img_gray[2719:2719+h, 2070:2070+w]
    # Q4_b
    img_box29 = img_gray[3338:3338+h, 390:390+w]
    img_box30 = img_gray[3443:3443+h, 390:390+w]
    img_box31 = img_gray[3548:3548+h, 390:390+w]
    img_box32 = img_gray[3653:3653+h, 390:390+w]
    img_box33 = img_gray[3756:3756+h, 390:390+w]
    img_box34 = img_gray[3861:3861+h, 390:390+w]
    img_box35 = img_gray[3966:3966+h, 390:390+w]
    img_box36 = img_gray[3338:3338+h, 2070:2070+w]
    img_box37 = img_gray[3443:3443+h, 2070:2070+w]
    img_box38 = img_gray[3547:3547+h, 2070:2070+w]
    img_box39 = img_gray[3653:3653+h, 2070:2070+w]
    img_box40 = img_gray[3756:3756+h, 2070:2070+w]
    img_box41 = img_gray[3861:3861+h, 2070:2070+w]
    img_box42 = img_gray[3966:3966+h, 2070:2070+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34, img_box35, img_box36,
                    img_box37, img_box38, img_box39, img_box40, img_box41, img_box42]

    # Boxes for choosing blank box
    img_list_blank = [img_box2, img_box3, img_box10, img_box12]

    # Boxes for choosing template
    img_list = [img_box13, img_box14]

    # Crop text image for Q4(a)&(b)
    textW1 = 325
    textW2 = 205
    textW3 = 460
    textH = 60

    AvgMonthIncomeText1 = img_gray[745:745+textH, 505:505+textW1]
    AvgMonthIncomeText2 = img_gray[745:745+textH, 1225:1225+textW2]
    AvgMonthIncomeText = [AvgMonthIncomeText1, AvgMonthIncomeText2]

    otherLiquidAssets1 = img_gray[1395:1395+textH, 370:370+textW3]
    otherLiquidAssets2 = img_gray[1395:1395+textH, 1110:1110+textW3]
    otherLiquidAssets = [otherLiquidAssets1, otherLiquidAssets2]

    liquidAssetsTotalText = img_gray[1445:1445+textH, 480:480+textW3]

    # Compare the similarities of boxes 2, 3, 10, 12, and choose the most similar pair
    res_blank = {}
    for index_1, img_1 in enumerate(img_list_blank):
        for index_2, img_2 in enumerate(img_list_blank):
            if index_1 >= index_2:
                pass
            else:
                corr = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
                res_blank[index_1] = corr  # Store similarity of each pair, and choose the index from one of both

    # Choose one of the images of the most similar pair as blankbox template
    max_blank_index = max(res_blank.items(), key=itemgetter(1))[0]
    img_blank = img_list_blank[max_blank_index]

    # Calculate the similarities between blank box and 2 boxes in question 4
    res_box = {}
    for index, img_box in enumerate(img_list):
        corr = cv.matchTemplate(img_box, img_blank, cv.TM_CCOEFF_NORMED)
        res_box[index] = corr

    # Choose the image with lowest correlation coefficient as template
    min_corr_index = min(res_box.items(), key=itemgetter(1))[0]
    template = img_list[min_corr_index]

    # Compare all the boxes and extract the relevant info
    res_all = []
    for i in img_box_list:
        res_all.append(cv.matchTemplate(i, template, cv.TM_CCOEFF_NORMED))

    # Specify a similarity threshold
    threshold = 0.75

    policyTarget = ""
    IsRegularIncome = ""
    AvgMonthIncome = ""
    liquidAssets = ""
    text = ""
    text2 = ""
    res_temp = [-1]
    res_temp2 = [-1]
    res_temp3 = [-1]
    res_temp4_1 = []
    res_temp4_2 = []
    res_temp4_3 = []
    res_temp4_4 = []
    res_temp4_5 = []
    res_temp4_6 = []
    res_temp4_7 = []
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 11 and similarity > max(res_temp):
                if index == 0 or index == 6:
                    policyTarget = textData.iloc[23][1]
                    res_temp.append(similarity)
                elif index == 1 or index == 7:
                    policyTarget = textData.iloc[24][1]
                    res_temp.append(similarity)
                elif index == 2 or index == 8:
                    policyTarget = textData.iloc[25][1]
                    res_temp.append(similarity)
                elif index == 3 or index == 9:
                    policyTarget = textData.iloc[26][1]
                    res_temp.append(similarity)
                elif index == 4 or index == 10:
                    policyTarget = textData.iloc[27][1]
                    res_temp.append(similarity)
                elif index == 5 or index == 11:
                    policyTarget = textData.iloc[28][1]
                    res_temp.append(similarity)
                else:
                    pass
            if 12 <= index <= 13 and similarity > max(res_temp2):
                if index == 12:
                    IsRegularIncome = textData.iloc[29][1]
                    res_temp2.append(similarity)
                elif index == 13:
                    IsRegularIncome = textData.iloc[30][1]
                    res_temp2.append(similarity)
                else:
                    pass
            if 14 <= index <= 27 and similarity > max(res_temp3):
                if index == 14 or index == 15:
                    #for i in AvgMonthIncomeText:
                    #    tmp = pytesseract.image_to_string(i, lang='chi_tra')
                    #    text = text + tmp + '    '
                    AvgMonthIncome = textData.iloc[31][1]# + text
                    res_temp3.append(similarity)
                elif index == 18 or index == 23:
                    AvgMonthIncome = textData.iloc[32][1]
                    res_temp3.append(similarity)
                elif index == 19 or index == 24:
                    AvgMonthIncome = textData.iloc[33][1]
                    res_temp3.append(similarity)
                elif index == 20 or index == 25:
                    AvgMonthIncome = textData.iloc[34][1]
                    res_temp3.append(similarity)
                elif index == 21 or index == 26:
                    AvgMonthIncome = textData.iloc[35][1]
                    res_temp3.append(similarity)
                elif index == 22 or index == 27:
                    AvgMonthIncome = textData.iloc[36][1]
                    res_temp3.append(similarity)
                else:
                    pass
            if 28 <= index <= 41:
                if index == 28 or index == 35:
                    if not res_temp4_1:
                        liquidAssets = liquidAssets + textData.iloc[37][1] + '    '
                        res_temp4_1.append(similarity)
                    else:
                        pass
                elif index == 29 or index == 36:
                    if not res_temp4_2:
                        liquidAssets = liquidAssets + textData.iloc[38][1] + '    '
                        res_temp4_2.append(similarity)
                    else:
                        pass
                elif index == 30 or index == 37:
                    if not res_temp4_3:
                        liquidAssets = liquidAssets + textData.iloc[39][1] + '    '
                        res_temp4_3.append(similarity)
                    else:
                        pass
                elif index == 31 or index == 38:
                    if not res_temp4_4:
                        liquidAssets = liquidAssets + textData.iloc[40][1] + '    '
                        res_temp4_4.append(similarity)
                    else:
                        pass
                elif index == 32 or index == 39:
                    if not res_temp4_5:
                        liquidAssets = liquidAssets + textData.iloc[41][1] + '    '
                        res_temp4_5.append(similarity)
                    else:
                        pass
                elif index == 33 or index == 40:
                    if not res_temp4_6:
                        liquidAssets = liquidAssets + textData.iloc[42][1] + '    '
                        res_temp4_6.append(similarity)
                    else:
                        pass
                elif index == 34 or index == 41:
                    #for n in otherLiquidAssets:
                        #tmp2 = pytesseract.image_to_string(n, lang='chi_tra')
                        #text2 = text2 + tmp2 + '    '
                    if not res_temp4_7:
                        liquidAssets = liquidAssets + textData.iloc[43][1] + '    '# + text2
                        res_temp4_7.append(similarity)
                    else:
                        pass
                else:
                    pass
        else:
            pass

    # Scan texts of total liquid assets amount
    liquidAssetsTotal = pytesseract.image_to_string(liquidAssetsTotalText)#, lang='chi_tra')

    return policyTarget, IsRegularIncome, AvgMonthIncome, liquidAssets, liquidAssetsTotal
