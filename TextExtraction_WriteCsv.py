import os
import csv


def write_csv(answerList, output_dir, user_index):
    # Headers for csv output
    header_row = ['policy_num', 'page', 'question', 'answer']

    # Write csv output
    with open(os.path.join(output_dir, user_index+'.csv'), 'w') as f:
        # Wrap file with a csv.writer
        writer = csv.writer(f, lineterminator='\n')

        # Write header
        writer.writerow(header_row)

        # Write row data
        # Page1
        writer.writerow([user_index, '1', 'maritalStatus', answerList[0][0]])
        writer.writerow([user_index, '1', 'noOfDependents', answerList[0][1]])
        writer.writerow([user_index, '1', 'educationLevel', answerList[0][2]])
        writer.writerow([user_index, '1', 'FNA_PRODUCT_PURPOSE', answerList[0][3]])
        writer.writerow([user_index, '1', 'FNA_PRODUCT_TYPE', answerList[0][4]])
        # Page2
        writer.writerow([user_index, '2', 'FNA_POLICY_TARGET_HORIZON', answerList[1][0]])
        writer.writerow([user_index, '2', 'FNA_IS_REGULAR_INCOME', answerList[1][1]])
        writer.writerow([user_index, '2', 'FNA_AVG_MONTH_INCOME', answerList[1][2]])
        writer.writerow([user_index, '2', 'FNA_AMOUNT_OF_LIQUID_ASSETS', answerList[1][3]])
        #writer.writerow([user_index, '2', 'FNA_LIQUID_ASSETS_TOTAL', answerList[1][4]])
        # Page3
        writer.writerow([user_index, '3', 'FNA_GOAL_DURATION', answerList[2][0]])
        writer.writerow([user_index, '3', 'FNA_INCOME_PERCENT_FOR_PREMIUM', answerList[2][1]])
        writer.writerow([user_index, '3', 'FNA_FUND_SOURCE', answerList[2][2]])
        # Page4
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_1', answerList[3][0]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_2', answerList[3][1]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_3', answerList[3][2]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_4', answerList[3][3]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_5', answerList[3][4]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_6', answerList[3][5]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_7', answerList[3][6]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_8', answerList[3][7]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_9', answerList[3][8]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_10', answerList[3][9]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_11', answerList[3][10]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_12', answerList[3][11]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_13', answerList[3][12]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_14', answerList[3][13]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_15', answerList[3][14]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_16', answerList[3][15]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_17', answerList[3][16]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_18', answerList[3][17]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_19', answerList[3][18]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q1_20', answerList[3][19]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_1', answerList[3][20]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_2', answerList[3][21]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_3', answerList[3][22]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_4', answerList[3][23]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_5', answerList[3][24]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_6', answerList[3][25]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_7', answerList[3][26]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_8', answerList[3][27]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_9', answerList[3][28]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_10', answerList[3][29]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_11', answerList[3][30]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_12', answerList[3][31]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_13', answerList[3][32]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_14', answerList[3][33]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_15', answerList[3][34]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_16', answerList[3][35]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_17', answerList[3][36]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_18', answerList[3][37]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_19', answerList[3][38]])
        writer.writerow([user_index, '4', 'INSURANCE_OPTION_Q2_20', answerList[3][39]])
        # Page5
        writer.writerow([user_index, '5', 'RISK_PROFILE_EDUCATION_LEVEL', answerList[4][0]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_INVESTMENT_EXPERIENCE', answerList[4][1]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_INVESTMENT_OBJECTIVE', answerList[4][2]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_RESERVED_LIQUID_ASSET', answerList[4][3]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_RETIRE_TIME', answerList[4][4]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_MONTHLY_INVESTMENT_PERCENT', answerList[4][5]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_FEELING_ATTITUDE', answerList[4][6]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_INVESTMENT_HOLD', answerList[4][7]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_WHEN_20_PERCENT_LOSS', answerList[4][8]])
        writer.writerow([user_index, '5', 'RISK_PROFILE_EXPECTED_RETURN', answerList[4][9]])
