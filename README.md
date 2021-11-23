# Insurance Advice Api



### Introduction

> This project provides an score based on user financial information.

### Running the project

- First you need to install python 3.7 version and pip in your machine.
- Python installed, now we need to run thw following command  `pip install -r requirements.txt ` on src/api/ directory to install all packages.
- The final step we need to run `python python insurance_api.py`


### Request to test

- Now calling the api http://127.0.0.1:5000/ , providing this body request, you are able to test the api.

`{
  "age": 61,
  "dependents": 2,
 "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "single",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}`





