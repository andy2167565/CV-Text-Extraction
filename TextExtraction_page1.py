import cv2 as cv
from operator import itemgetter


def page1(img_gray, textData):
    # Read all boxes in this page as input images for comparison
    # Left margin: 1~1.1 cm
    # Upper margin: 1~1.1 cm
    w = 80
    h = 80
    # Marital Status
    img_box1 = img_gray[1431:1431+h, 2884:2884+w]
    img_box2 = img_gray[1431:1431+h, 3315:3315+w]
    img_box3 = img_gray[1612:1612+h, 2884:2884+w]
    img_box4 = img_gray[1612:1612+h, 3315:3315+w]
    # No. of Dependents
    img_box5 = img_gray[1845:1845+h, 1076:1076+w]
    img_box6 = img_gray[1845:1845+h, 1562:1562+w]
    img_box7 = img_gray[1845:1845+h, 1911:1911+w]
    img_box8 = img_gray[1959:1959+h, 1076:1076+w]
    # Education Level
    img_box9 = img_gray[2258:2258+h, 1076:1076+w]
    img_box10 = img_gray[2258:2258+h, 2757:2757+w]
    img_box11 = img_gray[2392:2392+h, 1076:1076+w]
    img_box12 = img_gray[2392:2392+h, 2757:2757+w]
    # Q1
    img_box13 = img_gray[3282:3282+h, 388:388+w]
    img_box14 = img_gray[3395:3395+h, 388:388+w]
    img_box15 = img_gray[3508:3508+h, 388:388+w]
    img_box16 = img_gray[3622:3622+h, 388:388+w]
    img_box17 = img_gray[3734:3734+h, 388:388+w]
    img_box18 = img_gray[3847:3847+h, 388:388+w]
    img_box19 = img_gray[3282:3282+h, 2068:2068+w]
    img_box20 = img_gray[3395:3395+h, 2068:2068+w]
    img_box21 = img_gray[3508:3508+h, 2068:2068+w]
    img_box22 = img_gray[3622:3622+h, 2068:2068+w]
    img_box23 = img_gray[3734:3734+h, 2068:2068+w]
    img_box24 = img_gray[3847:3847+h, 2068:2068+w]
    # Q2
    img_box25 = img_gray[4345:4345+h, 388:388+w]
    img_box26 = img_gray[4541:4541+h, 388:388+w]
    img_box27 = img_gray[4738:4738+h, 388:388+w]
    img_box28 = img_gray[4935:4935+h, 388:388+w]
    img_box29 = img_gray[5130:5130+h, 388:388+w]
    img_box30 = img_gray[4345:4345+h, 2068:2068+w]
    img_box31 = img_gray[4541:4541+h, 2068:2068+w]
    img_box32 = img_gray[4738:4738+h, 2068:2068+w]
    img_box33 = img_gray[4935:4935+h, 2068:2068+w]
    img_box34 = img_gray[5130:5130+h, 2068:2068+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34]

    # Circles for choosing blank circle
    img_list_blank = [img_box1, img_box2, img_box3, img_box4]

    # Circles for choosing template
    img_list = [img_box9, img_box10, img_box11, img_box12]

    # Boxes for choosing blank box
    img_list_blank2 = [img_box25, img_box26, img_box33, img_box34]

    # Boxes for choosing template
    img_list2 = [img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                 img_box19, img_box20, img_box21, img_box22, img_box23, img_box24]

    '''
    Circle template
    '''
    # Compare the similarities of circles in Marital Status, and choose the most similar pair
    res_blank_circle = {}
    for index_1, img_1 in enumerate(img_list_blank):
        for index_2, img_2 in enumerate(img_list_blank):
            if index_1 >= index_2:
                pass
            else:
                corr = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
                res_blank_circle[index_1] = corr  # Store similarity of each pair, and choose the index from one of both

    # Choose one of the images of the most similar pair as blank circle template
    max_blank_circle_index = max(res_blank_circle.items(), key=itemgetter(1))[0]
    img_blank_circle = img_list_blank[max_blank_circle_index]

    # Calculate the similarities between blank circle and all the circles in Education Level
    res_circle = {}
    for index, img_box in enumerate(img_list):
        corr = cv.matchTemplate(img_box, img_blank_circle, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
        res_circle[index] = corr

    # Choose the image with lowest correlation coefficient as template
    min_corr_index = min(res_circle.items(), key=itemgetter(1))[0]
    template_circle = img_list[min_corr_index]

    '''
    Tick box template
    '''
    # Compare the similarities of 4 boxes in Q2, which are box 25, 26, 33, and 34, and choose the most similar pair
    res_blank_box = {}
    for index_1, img_1 in enumerate(img_list_blank2):
        for index_2, img_2 in enumerate(img_list_blank2):
            if index_1 >= index_2:
                pass
            else:
                corr = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
                res_blank_box[index_1] = corr

    # Choose one of the images of the most similar pair as blank box template
    max_blank_box_index = max(res_blank_box.items(), key=itemgetter(1))[0]
    img_blank_box = img_list_blank2[max_blank_box_index]

    # Calculate the similarities between blank box and all the boxes in Q1
    res_box = {}
    for index, img_box in enumerate(img_list2):
        corr = cv.matchTemplate(img_box, img_blank_box, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
        res_box[index] = corr

    # Choose the image with lowest correlation coefficient as template
    min_corr_index_2 = min(res_box.items(), key=itemgetter(1))[0]
    template_box = img_list2[min_corr_index_2]

    # Compare all the circles and boxes, and extract the relevant info
    res_all = []
    for index, img_box in enumerate(img_box_list):
        if 0 <= index <= 11:
            res_all.append(cv.matchTemplate(img_box, template_circle, cv.TM_CCOEFF_NORMED))
        else:
            res_all.append(cv.matchTemplate(img_box, template_box, cv.TM_CCOEFF_NORMED))

    # Specify a similarity threshold
    threshold = 0.8

    maritalStatus = ""
    noOfDependents = ""
    educationLevel = ""
    FNAProductPurpose = ""
    FNAProductType = ""
    res_temp = [-1]
    res_temp2 = [-1]
    res_temp3 = [-1]
    res_temp4_1 = []
    res_temp4_2 = []
    res_temp4_3 = []
    res_temp4_4 = []
    res_temp4_5 = []
    res_temp4_6 = []
    res_temp5_1 = []
    res_temp5_2 = []
    res_temp5_3 = []
    res_temp5_4 = []
    res_temp5_5 = []
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 3 and similarity > max(res_temp):
                if index == 0:
                    maritalStatus = textData.iloc[0][1]
                    res_temp.append(similarity)
                elif index == 1:
                    maritalStatus = textData.iloc[1][1]
                    res_temp.append(similarity)
                elif index == 2:
                    maritalStatus = textData.iloc[2][1]
                    res_temp.append(similarity)
                elif index == 3:
                    maritalStatus = textData.iloc[3][1]
                    res_temp.append(similarity)
                else:
                    pass
            elif 4 <= index <= 7 and similarity > max(res_temp2):
                if index == 4:
                    noOfDependents = textData.iloc[4][1]
                    res_temp2.append(similarity)
                elif index == 5:
                    noOfDependents = textData.iloc[5][1]
                    res_temp2.append(similarity)
                elif index == 6:
                    noOfDependents = textData.iloc[6][1]
                    res_temp2.append(similarity)
                elif index == 7:
                    noOfDependents = textData.iloc[7][1]
                    res_temp2.append(similarity)
                else:
                    pass
            elif 8 <= index <= 11 and similarity > max(res_temp3):
                if index == 8:
                    educationLevel = textData.iloc[8][1]
                    res_temp3.append(similarity)
                elif index == 9:
                    educationLevel = textData.iloc[9][1]
                    res_temp3.append(similarity)
                elif index == 10:
                    educationLevel = textData.iloc[10][1]
                    res_temp3.append(similarity)
                elif index == 11:
                    educationLevel = textData.iloc[11][1]
                    res_temp3.append(similarity)
                else:
                    pass
            elif 12 <= index <= 23:
                if index == 12 or index == 18:
                    # Prevent from being selected twice
                    if not res_temp4_1:  # If res_temp4_1 is empty
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[12][1] + '    '
                        res_temp4_1.append(similarity)
                    else:
                        pass
                elif index == 13 or index == 19:
                    if not res_temp4_2:
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[13][1] + '    '
                        res_temp4_2.append(similarity)
                    else:
                        pass
                elif index == 14 or index == 20:
                    if not res_temp4_3:
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[14][1] + '    '
                        res_temp4_3.append(similarity)
                    else:
                        pass
                elif index == 15 or index == 21:
                    if not res_temp4_4:
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[15][1] + '    '
                        res_temp4_4.append(similarity)
                    else:
                        pass
                elif index == 16 or index == 22:
                    if not res_temp4_5:
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[16][1] + '    '
                        res_temp4_5.append(similarity)
                    else:
                        pass
                elif index == 17 or index == 23:
                    if not res_temp4_6:
                        FNAProductPurpose = FNAProductPurpose + textData.iloc[17][1] + '    '
                        res_temp4_6.append(similarity)
                    else:
                        pass
                else:
                    pass
            elif 24 <= index <= 33:
                if index == 24 or index == 29:
                    if not res_temp5_1:
                        FNAProductType = FNAProductType + textData.iloc[18][1] + '    '
                        res_temp5_1.append(similarity)
                    else:
                        pass
                elif index == 25 or index == 30:
                    if not res_temp5_2:
                        FNAProductType = FNAProductType + textData.iloc[19][1] + '    '
                        res_temp5_2.append(similarity)
                    else:
                        pass
                elif index == 26 or index == 31:
                    if not res_temp5_3:
                        FNAProductType = FNAProductType + textData.iloc[20][1] + '    '
                        res_temp5_3.append(similarity)
                    else:
                        pass
                elif index == 27 or index == 32:
                    if not res_temp5_4:
                        FNAProductType = FNAProductType + textData.iloc[21][1] + '    '
                        res_temp5_4.append(similarity)
                    else:
                        pass
                elif index == 28 or index == 33:
                    if not res_temp5_5:
                        FNAProductType = FNAProductType + textData.iloc[22][1] + '    '
                        res_temp5_5.append(similarity)
                    else:
                        pass
                else:
                    pass
        else:
            pass

    return maritalStatus, noOfDependents, educationLevel, FNAProductPurpose, FNAProductType
