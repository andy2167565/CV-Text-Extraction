# Computer Vision Text Extraction
Text Recognition and Extraction System on completed standard forms in image format using OCR and OpenCV

## Directory Structure
    .
    ├── configFile                                  # Contains all the configuration files required in the scripts
    │   ├── <FORM_OPTION_TEXT_FILENAME>.csv         # Contains answers for all tickbox and circle options, can be adjusted on demand
    │   └── requirements.txt                        # Required Python packages
    ├── inputs                                      # Contains input PDF files for capturing data
    ├── outputs                                     # Contains all the output csv and json (automatically generated)
    ├── userPolicyNums                              # Contains transformed input file page by page in TIFF format, sorted by user policy number (automatically generated)
    └── ...

## Logic Flow
1.	Execute TextExtraction_AllPages.py to trigger other scripts
2.	Read configuration from form option list file
3.	Scan and extract data from each page respectively
4.	Save extracted data as JSON and CSV files

## How to Execute
### Install packages
```
pip install -r requirements.txt
```

### Run the script
```
python TextExtraction_AllPages.py
```
***
Copyright © 2019 [Andy Lin](https://github.com/andy2167565). All rights reserved.
