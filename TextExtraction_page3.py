import cv2 as cv
from operator import itemgetter


def page3(img_gray, textData):
    # Read all boxes in this page as input images for comparison
    # Left margin: 1~1.1 cm
    # Upper margin: 1~1.1 cm
    w = 80
    h = 80
    # (e)
    img_box1 = img_gray[2133:2133+h, 388:388+w]
    img_box2 = img_gray[2237:2237+h, 388:388+w]
    img_box3 = img_gray[2343:2343+h, 388:388+w]
    img_box4 = img_gray[2447:2447+h, 388:388+w]
    img_box5 = img_gray[2551:2551+h, 388:388+w]
    img_box6 = img_gray[2655:2655+h, 388:388+w]
    img_box7 = img_gray[2133:2133+h, 2068:2068+w]
    img_box8 = img_gray[2237:2237+h, 2068:2068+w]
    img_box9 = img_gray[2342:2342+h, 2068:2068+w]
    img_box10 = img_gray[2446:2446+h, 2068:2068+w]
    img_box11 = img_gray[2551:2551+h, 2068:2068+w]
    img_box12 = img_gray[2655:2655+h, 2068:2068+w]
    # (f)
    img_box13 = img_gray[3038:3038+h, 388:388+w]
    img_box14 = img_gray[3143:3143+h, 388:388+w]
    img_box15 = img_gray[3247:3247+h, 388:388+w]
    img_box16 = img_gray[3353:3353+h, 388:388+w]
    img_box17 = img_gray[3456:3456+h, 388:388+w]
    img_box18 = img_gray[3561:3561+h, 388:388+w]
    img_box19 = img_gray[3038:3038+h, 2068:2068+w]
    img_box20 = img_gray[3143:3143+h, 2068:2068+w]
    img_box21 = img_gray[3247:3247+h, 2068:2068+w]
    img_box22 = img_gray[3353:3353+h, 2068:2068+w]
    img_box23 = img_gray[3456:3456+h, 2068:2068+w]
    img_box24 = img_gray[3561:3561+h, 2068:2068+w]
    # (g)
    img_box25 = img_gray[3865:3865+h, 388:388+w]
    img_box26 = img_gray[3970:3970+h, 388:388+w]
    img_box27 = img_gray[4074:4074+h, 388:388+w]
    img_box28 = img_gray[4179:4179+h, 388:388+w]
    img_box29 = img_gray[4283:4283+h, 388:388+w]
    img_box30 = img_gray[3865:3865+h, 2068:2068+w]
    img_box31 = img_gray[3970:3970+h, 2068:2068+w]
    img_box32 = img_gray[4074:4074+h, 2068:2068+w]
    img_box33 = img_gray[4179:4179+h, 2068:2068+w]
    img_box34 = img_gray[4283:4283+h, 2068:2068+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34]

    # Boxes for choosing blank box
    img_list_blank = [img_box14, img_box15, img_box23, img_box24]

    # Boxes for choosing template
    img_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                img_box7, img_box8, img_box9, img_box10, img_box11, img_box12]

    # Compare the similarities of boxes 14, 15, 23, 24 in (f), and choose the most similar pair
    res_blank = {}
    for index_1, img_1 in enumerate(img_list_blank):
        for index_2, img_2 in enumerate(img_list_blank):
            if index_1 >= index_2:
                pass
            else:
                corr = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
                res_blank[index_1] = corr  # Store similarity of each pair, and choose the index from one of both

    # Choose one of the images of the most similar pair as blankbox template
    max_blank_index = max(res_blank.items(), key=itemgetter(1))[0]
    img_blank = img_list_blank[max_blank_index]

    # Calculate the similarities between blank box and all boxes in (e)
    res_box = {}
    for index, img_box in enumerate(img_list):
        corr = cv.matchTemplate(img_box, img_blank, cv.TM_CCOEFF_NORMED)  # (input image, template, method：比較方法)
        res_box[index] = corr

    # Choose the image with lowest correlation coefficient as template
    min_corr_index = min(res_box.items(), key=itemgetter(1))[0]
    template = img_list[min_corr_index]

    # Compare all the boxes and extract the relevant info
    res_all = []
    for i in img_box_list:
        res_all.append(cv.matchTemplate(i, template, cv.TM_CCOEFF_NORMED))

    # Specify a similarity threshold
    threshold = 0.85

    GoalDuration = ""
    IncomePercentForPremium = ""
    FundSource = ""
    res_temp = [-1]
    res_temp2 = [-1]
    res_temp3_1 = []
    res_temp3_2 = []
    res_temp3_3 = []
    res_temp3_4 = []
    res_temp3_5 = []
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 11 and similarity > max(res_temp):
                if index == 0 or index == 6:
                    GoalDuration = textData.iloc[44][1]
                    res_temp.append(similarity)
                elif index == 1 or index == 7:
                    GoalDuration = textData.iloc[45][1]
                    res_temp.append(similarity)
                elif index == 2 or index == 8:
                    GoalDuration = textData.iloc[46][1]
                    res_temp.append(similarity)
                elif index == 3 or index == 9:
                    GoalDuration = textData.iloc[47][1]
                    res_temp.append(similarity)
                elif index == 4 or index == 10:
                    GoalDuration = textData.iloc[48][1]
                    res_temp.append(similarity)
                elif index == 5 or index == 11:
                    GoalDuration = textData.iloc[49][1]
                    res_temp.append(similarity)
                else:
                    pass
            if 12 <= index <= 23 and similarity > max(res_temp2):
                if index == 12 or index == 18:
                    IncomePercentForPremium = textData.iloc[50][1]
                    res_temp2.append(similarity)
                elif index == 13 or index == 19:
                    IncomePercentForPremium = textData.iloc[51][1]
                    res_temp2.append(similarity)
                elif index == 14 or index == 20:
                    IncomePercentForPremium = textData.iloc[52][1]
                    res_temp2.append(similarity)
                elif index == 15 or index == 21:
                    IncomePercentForPremium = textData.iloc[53][1]
                    res_temp2.append(similarity)
                elif index == 16 or index == 22:
                    IncomePercentForPremium = textData.iloc[54][1]
                    res_temp2.append(similarity)
                elif index == 17 or index == 23:
                    IncomePercentForPremium = textData.iloc[55][1]
                    res_temp2.append(similarity)
                else:
                    pass
            if 24 <= index <= 33:
                if index == 24 or index == 29:
                    if not res_temp3_1:
                        FundSource = FundSource + textData.iloc[56][1] + '    '
                        res_temp3_1.append(similarity)
                    else:
                        pass
                elif index == 25 or index == 30:
                    if not res_temp3_2:
                        FundSource = FundSource + textData.iloc[57][1] + '    '
                        res_temp3_2.append(similarity)
                    else:
                        pass
                elif index == 26 or index == 31:
                    if not res_temp3_3:
                        FundSource = FundSource + textData.iloc[58][1] + '    '
                        res_temp3_3.append(similarity)
                    else:
                        pass
                elif index == 27 or index == 32:
                    if not res_temp3_4:
                        FundSource = FundSource + textData.iloc[59][1] + '    '
                        res_temp3_4.append(similarity)
                    else:
                        pass
                elif index == 28 or index == 33:
                    if not res_temp3_5:
                        FundSource = FundSource + textData.iloc[60][1] + '    '
                        res_temp3_5.append(similarity)
                    else:
                        pass
                else:
                    pass
        else:
            pass

    return GoalDuration, IncomePercentForPremium, FundSource
