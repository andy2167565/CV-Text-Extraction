import cv2 as cv
from operator import itemgetter


def page4_Q1(img_gray, textData):
    # Read all boxes in Q1 column as input images for comparison
    # Left margin: 1~1.1 cm
    # Upper margin: 1~1.1 cm
    w = 60
    h = 60
    # 5(Q1)a
    img_box1 = img_gray[1137:1137+h, 343:343+w]
    img_box2 = img_gray[1316:1316+h, 337:337+w]
    img_box3 = img_gray[1482:1482+h, 337:337+w]
    img_box4 = img_gray[1649:1649+h, 341:341+w]
    img_box5 = img_gray[1804:1804+h, 341:341+w]
    img_box6 = img_gray[1980:1980+h, 332:332+w]
    img_box7 = img_gray[2147:2147+h, 332:332+w]
    img_box8 = img_gray[2323:2323+h, 332:332+w]
    img_box9 = img_gray[2473:2473+h, 341:341+w]
    img_box10 = img_gray[2649:2649+h, 337:337+w]
    img_box11 = img_gray[2808:2808+h, 337:337+w]
    img_box12 = img_gray[2970:2970+h, 337:337+w]
    img_box13 = img_gray[3146:3146+h, 337:337+w]
    img_box14 = img_gray[3301:3301+h, 350:350+w]
    img_box15 = img_gray[3472:3472+h, 345:345+w]
    img_box16 = img_gray[3644:3644+h, 341:341+w]
    img_box17 = img_gray[3811:3811+h, 337:337+w]
    img_box18 = img_gray[3992:3992+h, 350:350+w]
    img_box19 = img_gray[4159:4159+h, 337:337+w]
    img_box20 = img_gray[4326:4326+h, 337:337+w]
    # 5(Q1)b
    img_box21 = img_gray[1137:1137+h, 636:636+w]
    img_box22 = img_gray[1316:1316+h, 630:630+w]
    img_box23 = img_gray[1482:1482+h, 630:630+w]
    img_box24 = img_gray[1649:1649+h, 634:634+w]
    img_box25 = img_gray[1804:1804+h, 634:634+w]
    img_box26 = img_gray[1980:1980+h, 625:625+w]
    img_box27 = img_gray[2147:2147+h, 625:625+w]
    img_box28 = img_gray[2323:2323+h, 625:625+w]
    img_box29 = img_gray[2473:2473+h, 634:634+w]
    img_box30 = img_gray[2649:2649+h, 630:630+w]
    img_box31 = img_gray[2808:2808+h, 630:630+w]
    img_box32 = img_gray[2970:2970+h, 630:630+w]
    img_box33 = img_gray[3146:3146+h, 630:630+w]
    img_box34 = img_gray[3301:3301+h, 643:643+w]
    img_box35 = img_gray[3472:3472+h, 638:638+w]
    img_box36 = img_gray[3644:3644+h, 634:634+w]
    img_box37 = img_gray[3811:3811+h, 630:630+w]
    img_box38 = img_gray[3992:3992+h, 643:643+w]
    img_box39 = img_gray[4159:4159+h, 630:630+w]
    img_box40 = img_gray[4326:4326+h, 630:630+w]
    # 5(Q1)c
    img_box41 = img_gray[1137:1137+h, 909:909+w]
    img_box42 = img_gray[1316:1316+h, 904:904+w]
    img_box43 = img_gray[1482:1482+h, 904:904+w]
    img_box44 = img_gray[1649:1649+h, 908:908+w]
    img_box45 = img_gray[1804:1804+h, 908:908+w]
    img_box46 = img_gray[1980:1980+h, 899:899+w]
    img_box47 = img_gray[2147:2147+h, 899:899+w]
    img_box48 = img_gray[2323:2323+h, 899:899+w]
    img_box49 = img_gray[2473:2473+h, 908:908+w]
    img_box50 = img_gray[2649:2649+h, 903:903+w]
    img_box51 = img_gray[2808:2808+h, 903:903+w]
    img_box52 = img_gray[2970:2970+h, 903:903+w]
    img_box53 = img_gray[3146:3146+h, 904:904+w]
    img_box54 = img_gray[3301:3301+h, 917:917+w]
    img_box55 = img_gray[3472:3472+h, 912:912+w]
    img_box56 = img_gray[3644:3644+h, 908:908+w]
    img_box57 = img_gray[3811:3811+h, 903:903+w]
    img_box58 = img_gray[3992:3992+h, 917:917+w]
    img_box59 = img_gray[4159:4159+h, 903:903+w]
    img_box60 = img_gray[4326:4326+h, 903:903+w]
    # 5(Q1)d
    img_box61 = img_gray[1223:1223+h, 346:346+w]
    img_box62 = img_gray[1403:1403+h, 341:341+w]
    img_box63 = img_gray[1569:1569+h, 340:340+w]
    img_box64 = img_gray[1736:1736+h, 345:345+w]
    img_box65 = img_gray[1891:1891+h, 345:345+w]
    img_box66 = img_gray[2066:2066+h, 336:336+w]
    img_box67 = img_gray[2234:2234+h, 336:336+w]
    img_box68 = img_gray[2410:2410+h, 336:336+w]
    img_box69 = img_gray[2560:2560+h, 345:345+w]
    img_box70 = img_gray[2736:2736+h, 340:340+w]
    img_box71 = img_gray[2894:2894+h, 340:340+w]
    img_box72 = img_gray[3057:3057+h, 340:340+w]
    img_box73 = img_gray[3233:3233+h, 340:340+w]
    img_box74 = img_gray[3387:3387+h, 353:353+w]
    img_box75 = img_gray[3559:3559+h, 349:349+w]
    img_box76 = img_gray[3731:3731+h, 345:345+w]
    img_box77 = img_gray[3898:3898+h, 340:340+w]
    img_box78 = img_gray[4078:4078+h, 353:353+w]
    img_box79 = img_gray[4246:4246+h, 340:340+w]
    img_box80 = img_gray[4413:4413+h, 340:340+w]
    # 5(Q1)e
    img_box81 = img_gray[1223:1223+h, 636:636+w]
    img_box82 = img_gray[1403:1403+h, 630:630+w]
    img_box83 = img_gray[1569:1569+h, 630:630+w]
    img_box84 = img_gray[1736:1736+h, 634:634+w]
    img_box85 = img_gray[1891:1891+h, 634:634+w]
    img_box86 = img_gray[2066:2066+h, 625:625+w]
    img_box87 = img_gray[2234:2234+h, 625:625+w]
    img_box88 = img_gray[2410:2410+h, 625:625+w]
    img_box89 = img_gray[2560:2560+h, 634:634+w]
    img_box90 = img_gray[2736:2736+h, 630:630+w]
    img_box91 = img_gray[2894:2894+h, 630:630+w]
    img_box92 = img_gray[3057:3057+h, 630:630+w]
    img_box93 = img_gray[3233:3233+h, 630:630+w]
    img_box94 = img_gray[3387:3387+h, 643:643+w]
    img_box95 = img_gray[3559:3559+h, 638:638+w]
    img_box96 = img_gray[3731:3731+h, 634:634+w]
    img_box97 = img_gray[3898:3898+h, 630:630+w]
    img_box98 = img_gray[4078:4078+h, 643:643+w]
    img_box99 = img_gray[4246:4246+h, 630:630+w]
    img_box100 = img_gray[4413:4413+h, 630:630+w]
    # 5(Q1)f
    img_box101 = img_gray[1223:1223+h, 902:902+w]
    img_box102 = img_gray[1403:1403+h, 897:897+w]
    img_box103 = img_gray[1569:1569+h, 897:897+w]
    img_box104 = img_gray[1736:1736+h, 901:901+w]
    img_box105 = img_gray[1891:1891+h, 901:901+w]
    img_box106 = img_gray[2066:2066+h, 892:892+w]
    img_box107 = img_gray[2234:2234+h, 892:892+w]
    img_box108 = img_gray[2410:2410+h, 892:892+w]
    img_box109 = img_gray[2560:2560+h, 901:901+w]
    img_box110 = img_gray[2736:2736+h, 897:897+w]
    img_box111 = img_gray[2894:2894+h, 897:897+w]
    img_box112 = img_gray[3057:3057+h, 897:897+w]
    img_box113 = img_gray[3233:3233+h, 897:897+w]
    img_box114 = img_gray[3387:3387+h, 910:910+w]
    img_box115 = img_gray[3559:3559+h, 905:905+w]
    img_box116 = img_gray[3731:3731+h, 901:901+w]
    img_box117 = img_gray[3898:3898+h, 897:897+w]
    img_box118 = img_gray[4078:4078+h, 910:910+w]
    img_box119 = img_gray[4246:4246+h, 897:897+w]
    img_box120 = img_gray[4413:4413+h, 896:896+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34, img_box35, img_box36,
                    img_box37, img_box38, img_box39, img_box40, img_box41, img_box42,
                    img_box43, img_box44, img_box45, img_box46, img_box47, img_box48,
                    img_box49, img_box50, img_box51, img_box52, img_box53, img_box54,
                    img_box55, img_box56, img_box57, img_box58, img_box59, img_box60,
                    img_box61, img_box62, img_box63, img_box64, img_box65, img_box66,
                    img_box67, img_box68, img_box69, img_box70, img_box71, img_box72,
                    img_box73, img_box74, img_box75, img_box76, img_box77, img_box78,
                    img_box79, img_box80, img_box81, img_box82, img_box83, img_box84,
                    img_box85, img_box86, img_box87, img_box88, img_box89, img_box90,
                    img_box91, img_box92, img_box93, img_box94, img_box95, img_box96,
                    img_box97, img_box98, img_box99, img_box100, img_box101, img_box102,
                    img_box103, img_box104, img_box105, img_box106, img_box107, img_box108,
                    img_box109, img_box110, img_box111, img_box112, img_box113, img_box114,
                    img_box115, img_box116, img_box117, img_box118, img_box119, img_box120]

    # Boxes for choosing blank box
    # All boxes in row20
    img_list_blank = [img_box20, img_box40, img_box60, img_box80, img_box100, img_box120]

    # Boxes for choosing template
    # All boxes in row1
    img_list = [img_box1, img_box21, img_box41, img_box61, img_box81, img_box101]

    # Compare the similarities of all boxes from 20th row, and choose the most similar pair
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

    # Calculate the similarities between blank box and all the boxes from 1st row
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
    threshold = 0.745

    Q1_1 = ""
    Q1_2 = ""
    Q1_3 = ""
    Q1_4 = ""
    Q1_5 = ""
    Q1_6 = ""
    Q1_7 = ""
    Q1_8 = ""
    Q1_9 = ""
    Q1_10 = ""
    Q1_11 = ""
    Q1_12 = ""
    Q1_13 = ""
    Q1_14 = ""
    Q1_15 = ""
    Q1_16 = ""
    Q1_17 = ""
    Q1_18 = ""
    Q1_19 = ""
    Q1_20 = ""
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 19:  # Option a
                if index == 0:
                    Q1_1 = Q1_1 + textData.iloc[61][1] + '    '
                elif index == 1:
                    Q1_2 = Q1_2 + textData.iloc[61][1] + '    '
                elif index == 2:
                    Q1_3 = Q1_3 + textData.iloc[61][1] + '    '
                elif index == 3:
                    Q1_4 = Q1_4 + textData.iloc[61][1] + '    '
                elif index == 4:
                    Q1_5 = Q1_5 + textData.iloc[61][1] + '    '
                elif index == 5:
                    Q1_6 = Q1_6 + textData.iloc[61][1] + '    '
                elif index == 6:
                    Q1_7 = Q1_7 + textData.iloc[61][1] + '    '
                elif index == 7:
                    Q1_8 = Q1_8 + textData.iloc[61][1] + '    '
                elif index == 8:
                    Q1_9 = Q1_9 + textData.iloc[61][1] + '    '
                elif index == 9:
                    Q1_10 = Q1_10 + textData.iloc[61][1] + '    '
                elif index == 10:
                    Q1_11 = Q1_11 + textData.iloc[61][1] + '    '
                elif index == 11:
                    Q1_12 = Q1_12 + textData.iloc[61][1] + '    '
                elif index == 12:
                    Q1_13 = Q1_13 + textData.iloc[61][1] + '    '
                elif index == 13:
                    Q1_14 = Q1_14 + textData.iloc[61][1] + '    '
                elif index == 14:
                    Q1_15 = Q1_15 + textData.iloc[61][1] + '    '
                elif index == 15:
                    Q1_16 = Q1_16 + textData.iloc[61][1] + '    '
                elif index == 16:
                    Q1_17 = Q1_17 + textData.iloc[61][1] + '    '
                elif index == 17:
                    Q1_18 = Q1_18 + textData.iloc[61][1] + '    '
                elif index == 18:
                    Q1_19 = Q1_19 + textData.iloc[61][1] + '    '
                elif index == 19:
                    Q1_20 = Q1_20 + textData.iloc[61][1] + '    '
                else:
                    pass
            elif 20 <= index <= 39:  # Option b
                if index == 20:
                    Q1_1 = Q1_1 + textData.iloc[62][1] + '    '
                elif index == 21:
                    Q1_2 = Q1_2 + textData.iloc[62][1] + '    '
                elif index == 22:
                    Q1_3 = Q1_3 + textData.iloc[62][1] + '    '
                elif index == 23:
                    Q1_4 = Q1_4 + textData.iloc[62][1] + '    '
                elif index == 24:
                    Q1_5 = Q1_5 + textData.iloc[62][1] + '    '
                elif index == 25:
                    Q1_6 = Q1_6 + textData.iloc[62][1] + '    '
                elif index == 26:
                    Q1_7 = Q1_7 + textData.iloc[62][1] + '    '
                elif index == 27:
                    Q1_8 = Q1_8 + textData.iloc[62][1] + '    '
                elif index == 28:
                    Q1_9 = Q1_9 + textData.iloc[62][1] + '    '
                elif index == 29:
                    Q1_10 = Q1_10 + textData.iloc[62][1] + '    '
                elif index == 30:
                    Q1_11 = Q1_11 + textData.iloc[62][1] + '    '
                elif index == 31:
                    Q1_12 = Q1_12 + textData.iloc[62][1] + '    '
                elif index == 32:
                    Q1_13 = Q1_13 + textData.iloc[62][1] + '    '
                elif index == 33:
                    Q1_14 = Q1_14 + textData.iloc[62][1] + '    '
                elif index == 34:
                    Q1_15 = Q1_15 + textData.iloc[62][1] + '    '
                elif index == 35:
                    Q1_16 = Q1_16 + textData.iloc[62][1] + '    '
                elif index == 36:
                    Q1_17 = Q1_17 + textData.iloc[62][1] + '    '
                elif index == 37:
                    Q1_18 = Q1_18 + textData.iloc[62][1] + '    '
                elif index == 38:
                    Q1_19 = Q1_19 + textData.iloc[62][1] + '    '
                elif index == 39:
                    Q1_20 = Q1_20 + textData.iloc[62][1] + '    '
                else:
                    pass
            elif 40 <= index <= 59:  # Option c
                if index == 40:
                    Q1_1 = Q1_1 + textData.iloc[63][1] + '    '
                elif index == 41:
                    Q1_2 = Q1_2 + textData.iloc[63][1] + '    '
                elif index == 42:
                    Q1_3 = Q1_3 + textData.iloc[63][1] + '    '
                elif index == 43:
                    Q1_4 = Q1_4 + textData.iloc[63][1] + '    '
                elif index == 44:
                    Q1_5 = Q1_5 + textData.iloc[63][1] + '    '
                elif index == 45:
                    Q1_6 = Q1_6 + textData.iloc[63][1] + '    '
                elif index == 46:
                    Q1_7 = Q1_7 + textData.iloc[63][1] + '    '
                elif index == 47:
                    Q1_8 = Q1_8 + textData.iloc[63][1] + '    '
                elif index == 48:
                    Q1_9 = Q1_9 + textData.iloc[63][1] + '    '
                elif index == 49:
                    Q1_10 = Q1_10 + textData.iloc[63][1] + '    '
                elif index == 50:
                    Q1_11 = Q1_11 + textData.iloc[63][1] + '    '
                elif index == 51:
                    Q1_12 = Q1_12 + textData.iloc[63][1] + '    '
                elif index == 52:
                    Q1_13 = Q1_13 + textData.iloc[63][1] + '    '
                elif index == 53:
                    Q1_14 = Q1_14 + textData.iloc[63][1] + '    '
                elif index == 54:
                    Q1_15 = Q1_15 + textData.iloc[63][1] + '    '
                elif index == 55:
                    Q1_16 = Q1_16 + textData.iloc[63][1] + '    '
                elif index == 56:
                    Q1_17 = Q1_17 + textData.iloc[63][1] + '    '
                elif index == 57:
                    Q1_18 = Q1_18 + textData.iloc[63][1] + '    '
                elif index == 58:
                    Q1_19 = Q1_19 + textData.iloc[63][1] + '    '
                elif index == 59:
                    Q1_20 = Q1_20 + textData.iloc[63][1] + '    '
                else:
                    pass
            elif 60 <= index <= 79:  # Option d
                if index == 60:
                    Q1_1 = Q1_1 + textData.iloc[64][1] + '    '
                elif index == 61:
                    Q1_2 = Q1_2 + textData.iloc[64][1] + '    '
                elif index == 62:
                    Q1_3 = Q1_3 + textData.iloc[64][1] + '    '
                elif index == 63:
                    Q1_4 = Q1_4 + textData.iloc[64][1] + '    '
                elif index == 64:
                    Q1_5 = Q1_5 + textData.iloc[64][1] + '    '
                elif index == 65:
                    Q1_6 = Q1_6 + textData.iloc[64][1] + '    '
                elif index == 66:
                    Q1_7 = Q1_7 + textData.iloc[64][1] + '    '
                elif index == 67:
                    Q1_8 = Q1_8 + textData.iloc[64][1] + '    '
                elif index == 68:
                    Q1_9 = Q1_9 + textData.iloc[64][1] + '    '
                elif index == 69:
                    Q1_10 = Q1_10 + textData.iloc[64][1] + '    '
                elif index == 70:
                    Q1_11 = Q1_11 + textData.iloc[64][1] + '    '
                elif index == 71:
                    Q1_12 = Q1_12 + textData.iloc[64][1] + '    '
                elif index == 72:
                    Q1_13 = Q1_13 + textData.iloc[64][1] + '    '
                elif index == 73:
                    Q1_14 = Q1_14 + textData.iloc[64][1] + '    '
                elif index == 74:
                    Q1_15 = Q1_15 + textData.iloc[64][1] + '    '
                elif index == 75:
                    Q1_16 = Q1_16 + textData.iloc[64][1] + '    '
                elif index == 76:
                    Q1_17 = Q1_17 + textData.iloc[64][1] + '    '
                elif index == 77:
                    Q1_18 = Q1_18 + textData.iloc[64][1] + '    '
                elif index == 78:
                    Q1_19 = Q1_19 + textData.iloc[64][1] + '    '
                elif index == 79:
                    Q1_20 = Q1_20 + textData.iloc[64][1] + '    '
                else:
                    pass
            elif 80 <= index <= 99:  # Option e
                if index == 80:
                    Q1_1 = Q1_1 + textData.iloc[65][1] + '    '
                elif index == 81:
                    Q1_2 = Q1_2 + textData.iloc[65][1] + '    '
                elif index == 82:
                    Q1_3 = Q1_3 + textData.iloc[65][1] + '    '
                elif index == 83:
                    Q1_4 = Q1_4 + textData.iloc[65][1] + '    '
                elif index == 84:
                    Q1_5 = Q1_5 + textData.iloc[65][1] + '    '
                elif index == 85:
                    Q1_6 = Q1_6 + textData.iloc[65][1] + '    '
                elif index == 86:
                    Q1_7 = Q1_7 + textData.iloc[65][1] + '    '
                elif index == 87:
                    Q1_8 = Q1_8 + textData.iloc[65][1] + '    '
                elif index == 88:
                    Q1_9 = Q1_9 + textData.iloc[65][1] + '    '
                elif index == 89:
                    Q1_10 = Q1_10 + textData.iloc[65][1] + '    '
                elif index == 90:
                    Q1_11 = Q1_11 + textData.iloc[65][1] + '    '
                elif index == 91:
                    Q1_12 = Q1_12 + textData.iloc[65][1] + '    '
                elif index == 92:
                    Q1_13 = Q1_13 + textData.iloc[65][1] + '    '
                elif index == 93:
                    Q1_14 = Q1_14 + textData.iloc[65][1] + '    '
                elif index == 94:
                    Q1_15 = Q1_15 + textData.iloc[65][1] + '    '
                elif index == 95:
                    Q1_16 = Q1_16 + textData.iloc[65][1] + '    '
                elif index == 96:
                    Q1_17 = Q1_17 + textData.iloc[65][1] + '    '
                elif index == 97:
                    Q1_18 = Q1_18 + textData.iloc[65][1] + '    '
                elif index == 98:
                    Q1_19 = Q1_19 + textData.iloc[65][1] + '    '
                elif index == 99:
                    Q1_20 = Q1_20 + textData.iloc[65][1] + '    '
                else:
                    pass
            elif 100 <= index <= 119:  # Option f
                if index == 100:
                    Q1_1 = Q1_1 + textData.iloc[66][1] + '    '
                elif index == 101:
                    Q1_2 = Q1_2 + textData.iloc[66][1] + '    '
                elif index == 102:
                    Q1_3 = Q1_3 + textData.iloc[66][1] + '    '
                elif index == 103:
                    Q1_4 = Q1_4 + textData.iloc[66][1] + '    '
                elif index == 104:
                    Q1_5 = Q1_5 + textData.iloc[66][1] + '    '
                elif index == 105:
                    Q1_6 = Q1_6 + textData.iloc[66][1] + '    '
                elif index == 106:
                    Q1_7 = Q1_7 + textData.iloc[66][1] + '    '
                elif index == 107:
                    Q1_8 = Q1_8 + textData.iloc[66][1] + '    '
                elif index == 108:
                    Q1_9 = Q1_9 + textData.iloc[66][1] + '    '
                elif index == 109:
                    Q1_10 = Q1_10 + textData.iloc[66][1] + '    '
                elif index == 110:
                    Q1_11 = Q1_11 + textData.iloc[66][1] + '    '
                elif index == 111:
                    Q1_12 = Q1_12 + textData.iloc[66][1] + '    '
                elif index == 112:
                    Q1_13 = Q1_13 + textData.iloc[66][1] + '    '
                elif index == 113:
                    Q1_14 = Q1_14 + textData.iloc[66][1] + '    '
                elif index == 114:
                    Q1_15 = Q1_15 + textData.iloc[66][1] + '    '
                elif index == 115:
                    Q1_16 = Q1_16 + textData.iloc[66][1] + '    '
                elif index == 116:
                    Q1_17 = Q1_17 + textData.iloc[66][1] + '    '
                elif index == 117:
                    Q1_18 = Q1_18 + textData.iloc[66][1] + '    '
                elif index == 118:
                    Q1_19 = Q1_19 + textData.iloc[66][1] + '    '
                elif index == 119:
                    Q1_20 = Q1_20 + textData.iloc[66][1] + '    '
                else:
                    pass
        else:
            pass

    return Q1_1, Q1_2, Q1_3, Q1_4, Q1_5, Q1_6, Q1_7, Q1_8, Q1_9, Q1_10, \
           Q1_11, Q1_12, Q1_13, Q1_14, Q1_15, Q1_16, Q1_17, Q1_18, Q1_19, Q1_20


def page4_Q2(img_gray, textData):
    # Read all boxes in Q2 column as input images for comparison
    # Left margin: 0.6 cm
    # Upper margin: 0.6 cm
    w = 40
    h = 40
    # 5(Q2)a
    img_box1 = img_gray[1151:1151+h, 1332:1332+w]
    img_box2 = img_gray[1318:1318+h, 1337:1337+w]
    img_box3 = img_gray[1490:1490+h, 1332:1332+w]
    img_box4 = img_gray[1639:1639+h, 1337:1337+w]
    img_box5 = img_gray[1807:1807+h, 1337:1337+w]
    img_box6 = img_gray[1983:1983+h, 1332:1332+w]
    img_box7 = img_gray[2159:2159+h, 1324:1324+w]
    img_box8 = img_gray[2321:2321+h, 1337:1337+w]
    img_box9 = img_gray[2485:2485+h, 1337:1337+w]
    img_box10 = img_gray[2660:2660+h, 1337:1337+w]
    img_box11 = img_gray[2832:2832+h, 1328:1328+w]
    img_box12 = img_gray[2999:2999+h, 1328:1328+w]
    img_box13 = img_gray[3149:3149+h, 1332:1332+w]
    img_box14 = img_gray[3317:3317+h, 1328:1328+w]
    img_box15 = img_gray[3488:3488+h, 1332:1332+w]
    img_box16 = img_gray[3656:3656+h, 1337:1337+w]
    img_box17 = img_gray[3827:3827+h, 1341:1341+w]
    img_box18 = img_gray[3991:3991+h, 1332:1332+w]
    img_box19 = img_gray[4154:4154+h, 1328:1328+w]
    img_box20 = img_gray[4321:4321+h, 1345:1345+w]
    # 5(Q2)b
    img_box21 = img_gray[1151:1151+h, 1532:1532+w]
    img_box22 = img_gray[1318:1318+h, 1536:1536+w]
    img_box23 = img_gray[1490:1490+h, 1532:1532+w]
    img_box24 = img_gray[1639:1639+h, 1536:1536+w]
    img_box25 = img_gray[1807:1807+h, 1536:1536+w]
    img_box26 = img_gray[1983:1983+h, 1532:1532+w]
    img_box27 = img_gray[2159:2159+h, 1523:1523+w]
    img_box28 = img_gray[2321:2321+h, 1536:1536+w]
    img_box29 = img_gray[2485:2485+h, 1536:1536+w]
    img_box30 = img_gray[2660:2660+h, 1536:1536+w]
    img_box31 = img_gray[2832:2832+h, 1527:1527+w]
    img_box32 = img_gray[2999:2999+h, 1527:1527+w]
    img_box33 = img_gray[3149:3149+h, 1532:1532+w]
    img_box34 = img_gray[3317:3317+h, 1527:1527+w]
    img_box35 = img_gray[3488:3488+h, 1532:1532+w]
    img_box36 = img_gray[3656:3656+h, 1536:1536+w]
    img_box37 = img_gray[3827:3827+h, 1540:1540+w]
    img_box38 = img_gray[3991:3991+h, 1532:1532+w]
    img_box39 = img_gray[4154:4154+h, 1527:1527+w]
    img_box40 = img_gray[4321:4321+h, 1544:1544+w]
    # 5(Q2)c
    img_box41 = img_gray[1151:1151+h, 1743:1743+w]
    img_box42 = img_gray[1318:1318+h, 1747:1747+w]
    img_box43 = img_gray[1490:1490+h, 1743:1743+w]
    img_box44 = img_gray[1639:1639+h, 1747:1747+w]
    img_box45 = img_gray[1807:1807+h, 1747:1747+w]
    img_box46 = img_gray[1983:1983+h, 1743:1743+w]
    img_box47 = img_gray[2159:2159+h, 1734:1734+w]
    img_box48 = img_gray[2321:2321+h, 1747:1747+w]
    img_box49 = img_gray[2485:2485+h, 1747:1747+w]
    img_box50 = img_gray[2660:2660+h, 1747:1747+w]
    img_box51 = img_gray[2832:2832+h, 1738:1738+w]
    img_box52 = img_gray[2999:2999+h, 1739:1739+w]
    img_box53 = img_gray[3149:3149+h, 1743:1743+w]
    img_box54 = img_gray[3317:3317+h, 1739:1739+w]
    img_box55 = img_gray[3488:3488+h, 1743:1743+w]
    img_box56 = img_gray[3656:3656+h, 1747:1747+w]
    img_box57 = img_gray[3827:3827+h, 1752:1752+w]
    img_box58 = img_gray[3991:3991+h, 1743:1743+w]
    img_box59 = img_gray[4154:4154+h, 1739:1739+w]
    img_box60 = img_gray[4321:4321+h, 1756:1756+w]
    # 5(Q2)d
    img_box61 = img_gray[1237:1237+h, 1336:1336+w]
    img_box62 = img_gray[1405:1405+h, 1340:1340+w]
    img_box63 = img_gray[1576:1576+h, 1336:1336+w]
    img_box64 = img_gray[1726:1726+h, 1340:1340+w]
    img_box65 = img_gray[1893:1893+h, 1340:1340+w]
    img_box66 = img_gray[2069:2069+h, 1336:1336+w]
    img_box67 = img_gray[2245:2245+h, 1327:1327+w]
    img_box68 = img_gray[2408:2408+h, 1340:1340+w]
    img_box69 = img_gray[2571:2571+h, 1340:1340+w]
    img_box70 = img_gray[2747:2747+h, 1340:1340+w]
    img_box71 = img_gray[2919:2919+h, 1331:1331+w]
    img_box72 = img_gray[3086:3086+h, 1332:1332+w]
    img_box73 = img_gray[3236:3236+h, 1336:1336+w]
    img_box74 = img_gray[3403:3403+h, 1332:1332+w]
    img_box75 = img_gray[3575:3575+h, 1336:1336+w]
    img_box76 = img_gray[3742:3742+h, 1340:1340+w]
    img_box77 = img_gray[3914:3914+h, 1345:1345+w]
    img_box78 = img_gray[4078:4078+h, 1336:1336+w]
    img_box79 = img_gray[4241:4241+h, 1332:1332+w]
    img_box80 = img_gray[4408:4408+h, 1349:1349+w]
    # 5(Q2)e
    img_box81 = img_gray[1237:1237+h, 1532:1532+w]
    img_box82 = img_gray[1405:1405+h, 1536:1536+w]
    img_box83 = img_gray[1576:1576+h, 1532:1532+w]
    img_box84 = img_gray[1726:1726+h, 1536:1536+w]
    img_box85 = img_gray[1893:1893+h, 1536:1536+w]
    img_box86 = img_gray[2069:2069+h, 1532:1532+w]
    img_box87 = img_gray[2245:2245+h, 1523:1523+w]
    img_box88 = img_gray[2408:2408+h, 1536:1536+w]
    img_box89 = img_gray[2571:2571+h, 1536:1536+w]
    img_box90 = img_gray[2747:2747+h, 1536:1536+w]
    img_box91 = img_gray[2919:2919+h, 1527:1527+w]
    img_box92 = img_gray[3086:3086+h, 1527:1527+w]
    img_box93 = img_gray[3236:3236+h, 1532:1532+w]
    img_box94 = img_gray[3403:3403+h, 1527:1527+w]
    img_box95 = img_gray[3575:3575+h, 1532:1532+w]
    img_box96 = img_gray[3742:3742+h, 1536:1536+w]
    img_box97 = img_gray[3914:3914+h, 1540:1540+w]
    img_box98 = img_gray[4078:4078+h, 1532:1532+w]
    img_box99 = img_gray[4241:4241+h, 1527:1527+w]
    img_box100 = img_gray[4408:4408+h, 1544:1544+w]

    # List of all boxes
    img_box_list = [img_box1, img_box2, img_box3, img_box4, img_box5, img_box6,
                    img_box7, img_box8, img_box9, img_box10, img_box11, img_box12,
                    img_box13, img_box14, img_box15, img_box16, img_box17, img_box18,
                    img_box19, img_box20, img_box21, img_box22, img_box23, img_box24,
                    img_box25, img_box26, img_box27, img_box28, img_box29, img_box30,
                    img_box31, img_box32, img_box33, img_box34, img_box35, img_box36,
                    img_box37, img_box38, img_box39, img_box40, img_box41, img_box42,
                    img_box43, img_box44, img_box45, img_box46, img_box47, img_box48,
                    img_box49, img_box50, img_box51, img_box52, img_box53, img_box54,
                    img_box55, img_box56, img_box57, img_box58, img_box59, img_box60,
                    img_box61, img_box62, img_box63, img_box64, img_box65, img_box66,
                    img_box67, img_box68, img_box69, img_box70, img_box71, img_box72,
                    img_box73, img_box74, img_box75, img_box76, img_box77, img_box78,
                    img_box79, img_box80, img_box81, img_box82, img_box83, img_box84,
                    img_box85, img_box86, img_box87, img_box88, img_box89, img_box90,
                    img_box91, img_box92, img_box93, img_box94, img_box95, img_box96,
                    img_box97, img_box98, img_box99, img_box100]

    # Boxes for choosing blank box
    # All boxes in row20
    img_list_blank = [img_box20, img_box40, img_box60, img_box80, img_box100]

    # Boxes for choosing template
    # All boxes in row1
    img_list = [img_box1, img_box21, img_box41, img_box61, img_box81]

    # Compare the similarities of boxes from 20th row -> a and c in Q1, d and e in Q2, and choose the most similar pair
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

    # Calculate the similarities between blank box and all the boxes from 1st row
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
    threshold = 0.8

    Q2_1 = ""
    Q2_2 = ""
    Q2_3 = ""
    Q2_4 = ""
    Q2_5 = ""
    Q2_6 = ""
    Q2_7 = ""
    Q2_8 = ""
    Q2_9 = ""
    Q2_10 = ""
    Q2_11 = ""
    Q2_12 = ""
    Q2_13 = ""
    Q2_14 = ""
    Q2_15 = ""
    Q2_16 = ""
    Q2_17 = ""
    Q2_18 = ""
    Q2_19 = ""
    Q2_20 = ""
    for index, similarity in enumerate(res_all):
        if similarity >= threshold:
            if 0 <= index <= 19:  # Option a
                if index == 0:
                    Q2_1 = Q2_1 + textData.iloc[61][1] + '    '
                elif index == 1:
                    Q2_2 = Q2_2 + textData.iloc[61][1] + '    '
                elif index == 2:
                    Q2_3 = Q2_3 + textData.iloc[61][1] + '    '
                elif index == 3:
                    Q2_4 = Q2_4 + textData.iloc[61][1] + '    '
                elif index == 4:
                    Q2_5 = Q2_5 + textData.iloc[61][1] + '    '
                elif index == 5:
                    Q2_6 = Q2_6 + textData.iloc[61][1] + '    '
                elif index == 6:
                    Q2_7 = Q2_7 + textData.iloc[61][1] + '    '
                elif index == 7:
                    Q2_8 = Q2_8 + textData.iloc[61][1] + '    '
                elif index == 8:
                    Q2_9 = Q2_9 + textData.iloc[61][1] + '    '
                elif index == 9:
                    Q2_10 = Q2_10 + textData.iloc[61][1] + '    '
                elif index == 10:
                    Q2_11 = Q2_11 + textData.iloc[61][1] + '    '
                elif index == 11:
                    Q2_12 = Q2_12 + textData.iloc[61][1] + '    '
                elif index == 12:
                    Q2_13 = Q2_13 + textData.iloc[61][1] + '    '
                elif index == 13:
                    Q2_14 = Q2_14 + textData.iloc[61][1] + '    '
                elif index == 14:
                    Q2_15 = Q2_15 + textData.iloc[61][1] + '    '
                elif index == 15:
                    Q2_16 = Q2_16 + textData.iloc[61][1] + '    '
                elif index == 16:
                    Q2_17 = Q2_17 + textData.iloc[61][1] + '    '
                elif index == 17:
                    Q2_18 = Q2_18 + textData.iloc[61][1] + '    '
                elif index == 18:
                    Q2_19 = Q2_19 + textData.iloc[61][1] + '    '
                elif index == 19:
                    Q2_20 = Q2_20 + textData.iloc[61][1] + '    '
                else:
                    pass
            elif 20 <= index <= 39:  # Option b
                if index == 20:
                    Q2_1 = Q2_1 + textData.iloc[62][1] + '    '
                elif index == 21:
                    Q2_2 = Q2_2 + textData.iloc[62][1] + '    '
                elif index == 22:
                    Q2_3 = Q2_3 + textData.iloc[62][1] + '    '
                elif index == 23:
                    Q2_4 = Q2_4 + textData.iloc[62][1] + '    '
                elif index == 24:
                    Q2_5 = Q2_5 + textData.iloc[62][1] + '    '
                elif index == 25:
                    Q2_6 = Q2_6 + textData.iloc[62][1] + '    '
                elif index == 26:
                    Q2_7 = Q2_7 + textData.iloc[62][1] + '    '
                elif index == 27:
                    Q2_8 = Q2_8 + textData.iloc[62][1] + '    '
                elif index == 28:
                    Q2_9 = Q2_9 + textData.iloc[62][1] + '    '
                elif index == 29:
                    Q2_10 = Q2_10 + textData.iloc[62][1] + '    '
                elif index == 30:
                    Q2_11 = Q2_11 + textData.iloc[62][1] + '    '
                elif index == 31:
                    Q2_12 = Q2_12 + textData.iloc[62][1] + '    '
                elif index == 32:
                    Q2_13 = Q2_13 + textData.iloc[62][1] + '    '
                elif index == 33:
                    Q2_14 = Q2_14 + textData.iloc[62][1] + '    '
                elif index == 34:
                    Q2_15 = Q2_15 + textData.iloc[62][1] + '    '
                elif index == 35:
                    Q2_16 = Q2_16 + textData.iloc[62][1] + '    '
                elif index == 36:
                    Q2_17 = Q2_17 + textData.iloc[62][1] + '    '
                elif index == 37:
                    Q2_18 = Q2_18 + textData.iloc[62][1] + '    '
                elif index == 38:
                    Q2_19 = Q2_19 + textData.iloc[62][1] + '    '
                elif index == 39:
                    Q2_20 = Q2_20 + textData.iloc[62][1] + '    '
                else:
                    pass
            elif 40 <= index <= 59:  # Option c
                if index == 40:
                    Q2_1 = Q2_1 + textData.iloc[63][1] + '    '
                elif index == 41:
                    Q2_2 = Q2_2 + textData.iloc[63][1] + '    '
                elif index == 42:
                    Q2_3 = Q2_3 + textData.iloc[63][1] + '    '
                elif index == 43:
                    Q2_4 = Q2_4 + textData.iloc[63][1] + '    '
                elif index == 44:
                    Q2_5 = Q2_5 + textData.iloc[63][1] + '    '
                elif index == 45:
                    Q2_6 = Q2_6 + textData.iloc[63][1] + '    '
                elif index == 46:
                    Q2_7 = Q2_7 + textData.iloc[63][1] + '    '
                elif index == 47:
                    Q2_8 = Q2_8 + textData.iloc[63][1] + '    '
                elif index == 48:
                    Q2_9 = Q2_9 + textData.iloc[63][1] + '    '
                elif index == 49:
                    Q2_10 = Q2_10 + textData.iloc[63][1] + '    '
                elif index == 50:
                    Q2_11 = Q2_11 + textData.iloc[63][1] + '    '
                elif index == 51:
                    Q2_12 = Q2_12 + textData.iloc[63][1] + '    '
                elif index == 52:
                    Q2_13 = Q2_13 + textData.iloc[63][1] + '    '
                elif index == 53:
                    Q2_14 = Q2_14 + textData.iloc[63][1] + '    '
                elif index == 54:
                    Q2_15 = Q2_15 + textData.iloc[63][1] + '    '
                elif index == 55:
                    Q2_16 = Q2_16 + textData.iloc[63][1] + '    '
                elif index == 56:
                    Q2_17 = Q2_17 + textData.iloc[63][1] + '    '
                elif index == 57:
                    Q2_18 = Q2_18 + textData.iloc[63][1] + '    '
                elif index == 58:
                    Q2_19 = Q2_19 + textData.iloc[63][1] + '    '
                elif index == 59:
                    Q2_20 = Q2_20 + textData.iloc[63][1] + '    '
                else:
                    pass
            elif 60 <= index <= 79:  # Option d
                if index == 60:
                    Q2_1 = Q2_1 + textData.iloc[64][1] + '    '
                elif index == 61:
                    Q2_2 = Q2_2 + textData.iloc[64][1] + '    '
                elif index == 62:
                    Q2_3 = Q2_3 + textData.iloc[64][1] + '    '
                elif index == 63:
                    Q2_4 = Q2_4 + textData.iloc[64][1] + '    '
                elif index == 64:
                    Q2_5 = Q2_5 + textData.iloc[64][1] + '    '
                elif index == 65:
                    Q2_6 = Q2_6 + textData.iloc[64][1] + '    '
                elif index == 66:
                    Q2_7 = Q2_7 + textData.iloc[64][1] + '    '
                elif index == 67:
                    Q2_8 = Q2_8 + textData.iloc[64][1] + '    '
                elif index == 68:
                    Q2_9 = Q2_9 + textData.iloc[64][1] + '    '
                elif index == 69:
                    Q2_10 = Q2_10 + textData.iloc[64][1] + '    '
                elif index == 70:
                    Q2_11 = Q2_11 + textData.iloc[64][1] + '    '
                elif index == 71:
                    Q2_12 = Q2_12 + textData.iloc[64][1] + '    '
                elif index == 72:
                    Q2_13 = Q2_13 + textData.iloc[64][1] + '    '
                elif index == 73:
                    Q2_14 = Q2_14 + textData.iloc[64][1] + '    '
                elif index == 74:
                    Q2_15 = Q2_15 + textData.iloc[64][1] + '    '
                elif index == 75:
                    Q2_16 = Q2_16 + textData.iloc[64][1] + '    '
                elif index == 76:
                    Q2_17 = Q2_17 + textData.iloc[64][1] + '    '
                elif index == 77:
                    Q2_18 = Q2_18 + textData.iloc[64][1] + '    '
                elif index == 78:
                    Q2_19 = Q2_19 + textData.iloc[64][1] + '    '
                elif index == 79:
                    Q2_20 = Q2_20 + textData.iloc[64][1] + '    '
                else:
                    pass
            elif 80 <= index <= 99:  # Option e
                if index == 80:
                    Q2_1 = Q2_1 + textData.iloc[65][1] + '    '
                elif index == 81:
                    Q2_2 = Q2_2 + textData.iloc[65][1] + '    '
                elif index == 82:
                    Q2_3 = Q2_3 + textData.iloc[65][1] + '    '
                elif index == 83:
                    Q2_4 = Q2_4 + textData.iloc[65][1] + '    '
                elif index == 84:
                    Q2_5 = Q2_5 + textData.iloc[65][1] + '    '
                elif index == 85:
                    Q2_6 = Q2_6 + textData.iloc[65][1] + '    '
                elif index == 86:
                    Q2_7 = Q2_7 + textData.iloc[65][1] + '    '
                elif index == 87:
                    Q2_8 = Q2_8 + textData.iloc[65][1] + '    '
                elif index == 88:
                    Q2_9 = Q2_9 + textData.iloc[65][1] + '    '
                elif index == 89:
                    Q2_10 = Q2_10 + textData.iloc[65][1] + '    '
                elif index == 90:
                    Q2_11 = Q2_11 + textData.iloc[65][1] + '    '
                elif index == 91:
                    Q2_12 = Q2_12 + textData.iloc[65][1] + '    '
                elif index == 92:
                    Q2_13 = Q2_13 + textData.iloc[65][1] + '    '
                elif index == 93:
                    Q2_14 = Q2_14 + textData.iloc[65][1] + '    '
                elif index == 94:
                    Q2_15 = Q2_15 + textData.iloc[65][1] + '    '
                elif index == 95:
                    Q2_16 = Q2_16 + textData.iloc[65][1] + '    '
                elif index == 96:
                    Q2_17 = Q2_17 + textData.iloc[65][1] + '    '
                elif index == 97:
                    Q2_18 = Q2_18 + textData.iloc[65][1] + '    '
                elif index == 98:
                    Q2_19 = Q2_19 + textData.iloc[65][1] + '    '
                elif index == 99:
                    Q2_20 = Q2_20 + textData.iloc[65][1] + '    '
                else:
                    pass
        else:
            pass

    return Q2_1, Q2_2, Q2_3, Q2_4, Q2_5, Q2_6, Q2_7, Q2_8, Q2_9, Q2_10,\
           Q2_11, Q2_12, Q2_13, Q2_14, Q2_15, Q2_16, Q2_17, Q2_18, Q2_19, Q2_20
