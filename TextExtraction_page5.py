import cv2 as cv
from operator import itemgetter


def page5(img_gray, textData):
    # Read all boxes in this page as input images for comparison
    # Left margin: 1~1.1 cm
    # Upper margin: 1~1.1 cm
    w = 80
    h = 80
    # Q1
    img_box1 = img_gray[436:436+h, 339:339+w]
    img_box2 = img_gray[507:507+h, 339:339+w]
    img_box3 = img_gray[578:578+h, 339:339+w]
    img_box4 = img_gray[720:720+h, 339:339+w]
    # Q2
    img_box5 = img_gray[1058:1058+h, 339:339+w]
    img_box6 = img_gray[1129:1129+h, 339:339+w]
    img_box7 = img_gray[1200:1200+h, 339:339+w]
    img_box8 = img_gray[1271:1271+h, 339:339+w]
    # Q3
    img_box9 = img_gray[1885:1885+h, 339:339+w]
    img_box10 = img_gray[1955:1955+h, 339:339+w]
    img_box11 = img_gray[2027:2027+h, 339:339+w]
    img_box12 = img_gray[2169:2169+h, 339:339+w]
    img_box13 = img_gray[2239:2239+h, 339:339+w]
    # Q4
    img_box14 = img_gray[2715:2715+h, 339:339+w]
    img_box15 = img_gray[2787:2787+h, 339:339+w]
    img_box16 = img_gray[2858:2858+h, 339:339+w]
    img_box17 = img_gray[2928:2928+h, 339:339+w]
    # Q5
    img_box18 = img_gray[3271:3271+h, 339:339+w]
    img_box19 = img_gray[3342:3342+h, 339:339+w]
    img_box20 = img_gray[3413:3413+h, 339:339+w]
    img_box21 = img_gray[3483:3483+h, 339:339+w]
    img_box22 = img_gray[3554:3554+h, 339:339+w]
    # Q6
    img_box23 = img_gray[508:508+h, 2101:2101+w]
    img_box24 = img_gray[578:578+h, 2101:2101+w]
    img_box25 = img_gray[648:648+h, 2101:2101+w]
    img_box26 = img_gray[719:719+h, 2101:2101+w]
    img_box27 = img_gray[791:791+h, 2101:2101+w]
    # Q7
    img_box28 = img_gray[1059:1059+h, 2101:2101+w]
    img_box29 = img_gray[1129:1129+h, 2101:2101+w]
    img_box30 = img_gray[1270:1270+h, 2101:2101+w]
    img_box31 = img_gray[1413:1413+h, 2101:2101+w]
    img_box32 = img_gray[1554:1554+h, 2101:2101+w]
    # Q8
    img_box33 = img_gray[1885:1885+h, 2101:2101+w]
    img_box34 = img_gray[1955:1955+h, 2101:2101+w]
    img_box35 = img_gray[2097:2097+h, 2101:2101+w]
    img_box36 = img_gray[2239:2239+h, 2101:2101+w]
    # Q9
    img_box37 = img_gray[2574:2574+h, 2101:2101+w]
    img_box38 = img_gray[2644:2644+h, 2101:2101+w]
    img_box39 = img_gray[2716:2716+h, 2101:2101+w]
    img_box40 = img_gray[2858:2858+h, 2101:2101+w]
    img_box41 = img_gray[2999:2999+h, 2101:2101+w]
    # Q10
    img_box42 = img_gray[3271:3271+h, 2101:2101+w]
    img_box43 = img_gray[3341:3341+h, 2101:2101+w]
    img_box44 = img_gray[3413:3413+h, 2101:2101+w]
    img_box45 = img_gray[3483:3483+h, 2101:2101+w]
    img_box46 = img_gray[3554:3554+h, 2101:2101+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34, img_box35, img_box36,
                    img_box37, img_box38, img_box39, img_box40, img_box41, img_box42,
                    img_box43, img_box44, img_box45, img_box46]

    # Circles for choosing blank circle
    img_list_blank = [img_box1, img_box2, img_box3, img_box4]

    # Circles for choosing template
    img_list = [img_box5, img_box6, img_box7, img_box8]

    # Compare the similarities of circles in Q1, and choose the most similar pair
    res_blank = {}
    for index_1, img_1 in enumerate(img_list_blank):
        for index_2, img_2 in enumerate(img_list_blank):
            if index_1 >= index_2:
                pass
            else:
                corr = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
                res_blank[index_1] = corr  # Store similarity of each pair, and choose the index from one of both

    # Choose one of the images of the most similar pair as blank circle template
    max_blank_index = max(res_blank.items(), key=itemgetter(1))[0]
    img_blank = img_list_blank[max_blank_index]

    # Calculate the similarities between blank circle and all the circles in Q2
    res_box = {}
    for index, img_box in enumerate(img_list):
        corr = cv.matchTemplate(img_box, img_blank, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
        res_box[index] = corr

    # Choose the image with lowest correlation coefficient as template
    min_corr_index = min(res_box.items(), key=itemgetter(1))[0]
    template = img_list[min_corr_index]

    # Compare all the circles and extract the relevant info
    res_all = []
    for i in img_box_list:
        res_all.append(cv.matchTemplate(i, template, cv.TM_CCOEFF_NORMED))

    # Specify a similarity threshold
    threshold = 0.7

    Q1 = ""
    Q2 = ""
    Q3 = ""
    Q4 = ""
    Q5 = ""
    Q6 = ""
    Q7 = ""
    Q8 = ""
    Q9 = ""
    Q10 = ""
    res_temp = [-1]
    res_temp2 = [-1]
    res_temp3 = [-1]
    res_temp4 = [-1]
    res_temp5 = [-1]
    res_temp6 = [-1]
    res_temp7 = [-1]
    res_temp8 = [-1]
    res_temp9 = [-1]
    res_temp10 = [-1]
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    counter_5 = 0
    counter_6 = 0
    counter_7 = 0
    counter_8 = 0
    counter_9 = 0
    counter_10 = 0
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 3 and similarity > max(res_temp):
                if index == 0:
                    Q1 = textData.iloc[67][1]
                    res_temp.append(similarity)
                    counter_1 += 1
                elif index == 1:
                    Q1 = textData.iloc[68][1]
                    res_temp.append(similarity)
                    counter_1 += 1
                elif index == 2:
                    Q1 = textData.iloc[69][1]
                    res_temp.append(similarity)
                    counter_1 += 1
                elif index == 3:
                    Q1 = textData.iloc[70][1]
                    res_temp.append(similarity)
                    counter_1 += 1
                else:
                    pass
            elif 4 <= index <= 7 and similarity > max(res_temp2):
                if index == 4:
                    Q2 = textData.iloc[71][1]
                    res_temp2.append(similarity)
                    counter_2 += 1
                elif index == 5:
                    Q2 = textData.iloc[72][1]
                    res_temp2.append(similarity)
                    counter_2 += 1
                elif index == 6:
                    Q2 = textData.iloc[73][1]
                    res_temp2.append(similarity)
                    counter_2 += 1
                elif index == 7:
                    Q2 = textData.iloc[74][1]
                    res_temp2.append(similarity)
                    counter_2 += 1
                else:
                    pass
            elif 8 <= index <= 12 and similarity > max(res_temp3):
                if index == 8:
                    Q3 = textData.iloc[75][1]
                    res_temp3.append(similarity)
                    counter_3 += 1
                elif index == 9:
                    Q3 = textData.iloc[76][1]
                    res_temp3.append(similarity)
                    counter_3 += 1
                elif index == 10:
                    Q3 = textData.iloc[77][1]
                    res_temp3.append(similarity)
                    counter_3 += 1
                elif index == 11:
                    Q3 = textData.iloc[78][1]
                    res_temp3.append(similarity)
                    counter_3 += 1
                elif index == 12:
                    Q3 = textData.iloc[79][1]
                    res_temp3.append(similarity)
                    counter_3 += 1
                else:
                    pass
            elif 13 <= index <= 16 and similarity > max(res_temp4):
                if index == 13:
                    Q4 = textData.iloc[80][1]
                    res_temp4.append(similarity)
                    counter_4 += 1
                elif index == 14:
                    Q4 = textData.iloc[81][1]
                    res_temp4.append(similarity)
                    counter_4 += 1
                elif index == 15:
                    Q4 = textData.iloc[82][1]
                    res_temp4.append(similarity)
                    counter_4 += 1
                elif index == 16:
                    Q4 = textData.iloc[83][1]
                    res_temp4.append(similarity)
                    counter_4 += 1
                else:
                    pass
            elif 17 <= index <= 21 and similarity > max(res_temp5):
                if index == 17:
                    Q5 = textData.iloc[84][1]
                    res_temp5.append(similarity)
                    counter_5 += 1
                elif index == 18:
                    Q5 = textData.iloc[85][1]
                    res_temp5.append(similarity)
                    counter_5 += 1
                elif index == 19:
                    Q5 = textData.iloc[86][1]
                    res_temp5.append(similarity)
                    counter_5 += 1
                elif index == 20:
                    Q5 = textData.iloc[87][1]
                    res_temp5.append(similarity)
                    counter_5 += 1
                elif index == 21:
                    Q5 = textData.iloc[88][1]
                    res_temp5.append(similarity)
                    counter_5 += 1
                else:
                    pass
            elif 22 <= index <= 26 and similarity > max(res_temp6):
                if index == 22:
                    Q6 = textData.iloc[89][1]
                    res_temp6.append(similarity)
                    counter_6 += 1
                elif index == 23:
                    Q6 = textData.iloc[90][1]
                    res_temp6.append(similarity)
                    counter_6 += 1
                elif index == 24:
                    Q6 = textData.iloc[91][1]
                    res_temp6.append(similarity)
                    counter_6 += 1
                elif index == 25:
                    Q6 = textData.iloc[92][1]
                    res_temp6.append(similarity)
                    counter_6 += 1
                elif index == 26:
                    Q6 = textData.iloc[93][1]
                    res_temp6.append(similarity)
                    counter_6 += 1
                else:
                    pass
            elif 27 <= index <= 31 and similarity > max(res_temp7):
                if index == 27:
                    Q7 = textData.iloc[94][1]
                    res_temp7.append(similarity)
                    counter_7 += 1
                elif index == 28:
                    Q7 = textData.iloc[95][1]
                    res_temp7.append(similarity)
                    counter_7 += 1
                elif index == 29:
                    Q7 = textData.iloc[96][1]
                    res_temp7.append(similarity)
                    counter_7 += 1
                elif index == 30:
                    Q7 = textData.iloc[97][1]
                    res_temp7.append(similarity)
                    counter_7 += 1
                elif index == 31:
                    Q7 = textData.iloc[98][1]
                    res_temp7.append(similarity)
                    counter_7 += 1
                else:
                    pass
            elif 32 <= index <= 35 and similarity > max(res_temp8):
                if index == 32:
                    Q8 = textData.iloc[99][1]
                    res_temp8.append(similarity)
                    counter_8 += 1
                elif index == 33:
                    Q8 = textData.iloc[100][1]
                    res_temp8.append(similarity)
                    counter_8 += 1
                elif index == 34:
                    Q8 = textData.iloc[101][1]
                    res_temp8.append(similarity)
                    counter_8 += 1
                elif index == 35:
                    Q8 = textData.iloc[102][1]
                    res_temp8.append(similarity)
                    counter_8 += 1
                else:
                    pass
            elif 36 <= index <= 40 and similarity > max(res_temp9):
                if index == 36:
                    Q9 = textData.iloc[103][1]
                    res_temp9.append(similarity)
                    counter_9 += 1
                elif index == 37:
                    Q9 = textData.iloc[104][1]
                    res_temp9.append(similarity)
                    counter_9 += 1
                elif index == 38:
                    Q9 = textData.iloc[105][1]
                    res_temp9.append(similarity)
                    counter_9 += 1
                elif index == 39:
                    Q9 = textData.iloc[106][1]
                    res_temp9.append(similarity)
                    counter_9 += 1
                elif index == 40:
                    Q9 = textData.iloc[107][1]
                    res_temp9.append(similarity)
                    counter_9 += 1
                else:
                    pass
            elif 41 <= index <= 45 and similarity > max(res_temp10):
                if index == 41:
                    Q10 = textData.iloc[108][1]
                    res_temp10.append(similarity)
                    counter_10 += 1
                elif index == 42:
                    Q10 = textData.iloc[109][1]
                    res_temp10.append(similarity)
                    counter_10 += 1
                elif index == 43:
                    Q10 = textData.iloc[110][1]
                    res_temp10.append(similarity)
                    counter_10 += 1
                elif index == 44:
                    Q10 = textData.iloc[111][1]
                    res_temp10.append(similarity)
                    counter_10 += 1
                elif index == 45:
                    Q10 = textData.iloc[112][1]
                    res_temp10.append(similarity)
                    counter_10 += 1
                else:
                    pass
        else:
            pass

    if counter_1 == 2:
        Q1 = ""
    if counter_2 == 2:
        Q2 = ""
    if counter_3 == 2:
        Q3 = ""
    if counter_4 == 2:
        Q4 = ""
    if counter_5 == 2:
        Q5 = ""
    if counter_6 == 1:
        Q6 = ""
    if counter_7 == 1:
        Q7 = ""
    if counter_8 == 1:
        Q8 = ""
    if counter_9 == 2:
        Q9 = ""
    if counter_10 == 2:
        Q10 = ""

    return Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
