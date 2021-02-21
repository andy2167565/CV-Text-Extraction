import os
import json
from datetime import datetime
from pytz import timezone


def write_json(answerList, output_dir, user_index):
    # Write json output
    source_id = <SOURCE_ID>
    fnaId = <FNA_ID>
    userId = <USER_ID>
    parentKey = <PARENT_KEY>
    versionID = 1
    signedDate = <SIGNED_DATE>

    fmt = "%Y-%m-%d %H:%M:%S %z"
    now_time = datetime.now(timezone('Asia/Hong_Kong'))
    systemCreatedDt = now_time.strftime(fmt)
    systemUpdatedDt = now_time.strftime(fmt)

    Class_Lead = <CLASS_LEAD>
    Class_Response = <CLASS_RESPONSE>

    data2 = {
        #"source_id": source_id,
        #"fnaId": fnaId,
        # Page1
        "maritalStatus": answerList[0][0],
        "noOfDependents": answerList[0][1],
        "educationLevel": answerList[0][2],
        "FNA_PRODUCT_PURPOSE": answerList[0][3],
        "FNA_PRODUCT_TYPE": answerList[0][4],
        # Page2
        "FNA_POLICY_TARGET_HORIZON": answerList[1][0],
        "FNA_IS_REGULAR_INCOME": answerList[1][1],
        "FNA_AVG_MONTH_INCOME": answerList[1][2],
        "FNA_AMOUNT_OF_LIQUID_ASSETS": answerList[1][3],
        #"FNA_LIQUID_ASSETS_TOTAL": answerList[1][4],
        # Page3
        "FNA_GOAL_DURATION": answerList[2][0],
        "FNA_INCOME_PERCENT_FOR_PREMIUM": answerList[2][1],
        "FNA_FUND_SOURCE": answerList[2][2],
        # Page4
        "INSURANCE_OPTION_Q1_1": answerList[3][0],
        "INSURANCE_OPTION_Q1_2": answerList[3][1],
        "INSURANCE_OPTION_Q1_3": answerList[3][2],
        "INSURANCE_OPTION_Q1_4": answerList[3][3],
        "INSURANCE_OPTION_Q1_5": answerList[3][4],
        "INSURANCE_OPTION_Q1_6": answerList[3][5],
        "INSURANCE_OPTION_Q1_7": answerList[3][6],
        "INSURANCE_OPTION_Q1_8": answerList[3][7],
        "INSURANCE_OPTION_Q1_9": answerList[3][8],
        "INSURANCE_OPTION_Q1_10": answerList[3][9],
        "INSURANCE_OPTION_Q1_11": answerList[3][10],
        "INSURANCE_OPTION_Q1_12": answerList[3][11],
        "INSURANCE_OPTION_Q1_13": answerList[3][12],
        "INSURANCE_OPTION_Q1_14": answerList[3][13],
        "INSURANCE_OPTION_Q1_15": answerList[3][14],
        "INSURANCE_OPTION_Q1_16": answerList[3][15],
        "INSURANCE_OPTION_Q1_17": answerList[3][16],
        "INSURANCE_OPTION_Q1_18": answerList[3][17],
        "INSURANCE_OPTION_Q1_19": answerList[3][18],
        "INSURANCE_OPTION_Q1_20": answerList[3][19],
        "INSURANCE_OPTION_Q2_1": answerList[3][20],
        "INSURANCE_OPTION_Q2_2": answerList[3][21],
        "INSURANCE_OPTION_Q2_3": answerList[3][22],
        "INSURANCE_OPTION_Q2_4": answerList[3][23],
        "INSURANCE_OPTION_Q2_5": answerList[3][24],
        "INSURANCE_OPTION_Q2_6": answerList[3][25],
        "INSURANCE_OPTION_Q2_7": answerList[3][26],
        "INSURANCE_OPTION_Q2_8": answerList[3][27],
        "INSURANCE_OPTION_Q2_9": answerList[3][28],
        "INSURANCE_OPTION_Q2_10": answerList[3][29],
        "INSURANCE_OPTION_Q2_11": answerList[3][30],
        "INSURANCE_OPTION_Q2_12": answerList[3][31],
        "INSURANCE_OPTION_Q2_13": answerList[3][32],
        "INSURANCE_OPTION_Q2_14": answerList[3][33],
        "INSURANCE_OPTION_Q2_15": answerList[3][34],
        "INSURANCE_OPTION_Q2_16": answerList[3][35],
        "INSURANCE_OPTION_Q2_17": answerList[3][36],
        "INSURANCE_OPTION_Q2_18": answerList[3][37],
        "INSURANCE_OPTION_Q2_19": answerList[3][38],
        "INSURANCE_OPTION_Q2_20": answerList[3][39],
        # Page5
        "RISK_PROFILE_EDUCATION_LEVEL": answerList[4][0],
        "RISK_PROFILE_INVESTMENT_EXPERIENCE": answerList[4][1],
        "RISK_PROFILE_INVESTMENT_OBJECTIVE": answerList[4][2],
        "RISK_PROFILE_RESERVED_LIQUID_ASSET": answerList[4][3],
        "RISK_PROFILE_RETIRE_TIME": answerList[4][4],
        "RISK_PROFILE_MONTHLY_INVESTMENT_PERCENT": answerList[4][5],
        "RISK_PROFILE_FEELING_ATTITUDE": answerList[4][6],
        "RISK_PROFILE_INVESTMENT_HOLD": answerList[4][7],
        "RISK_PROFILE_WHEN_20_PERCENT_LOSS": answerList[4][8],
        "RISK_PROFILE_EXPECTED_RETURN": answerList[4][9],
        #"userId": userId,
        #"parentKey": parentKey,
        #"versionID": versionID,
        "systemCreatedDt": systemCreatedDt,
        #"systemUpdatedDt": systemUpdatedDt,
        #"class": Class_Response
    }

    with open(os.path.join(output_dir, user_index+'.json'), 'w') as f:
        json.dump(data2, f, indent=8)
