# Steps need to follow to create a token:
# Read the CSV or Excel file.
# Create a function create_token which can take a value from the Excel file
# Verify the Expected Result

# Read the Excel--> openpyxl
import openpyxl
import requests
from src.constants.api_constants import APIConstants
from src.utils.utils import Util
from src.helpers.api_requests_wrapper_class import *


# Below are the 3 test cases which are important.
def read_credentials_from_excel(file_path):  # This will give you multiple data from Excel.
    credentials = []  # admin, pass123 etc. (which is created in Excel)
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


def create_auth_request(username,
                        password):  # This is to create an authentication, and we will call this method multiple times
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(url=APIConstants.url_create_token(),
                            headers=Util.common_headers_json(),
                            auth=None,
                            payload=payload,
                            in_json=False
                            )
    return response


def test_create_auth_with_excel():  # here I will write the logic.
    file_path = "C:\Users\Sharmvan\Py2xAPIAutomationFramework\pythonProject\tests\normal_CRUD_test_cases\datadriven testing\testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response=create_auth_request(username=username,password=password)
        print(response.status_code)