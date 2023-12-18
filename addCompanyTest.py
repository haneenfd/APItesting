import requests
from globalVariables import base_url, addCompanyAPI,universityUsername,password,jsonScheme
from loginTest import get_header
url = base_url + addCompanyAPI

def makeData(id,name,email,location,phoneNumber,managerName):
    data = {
        "id": id,
        "name": name,
        "email": email,
        "location": location,
        "phoneNumber": phoneNumber,
        "managerName": managerName
        }
    return data

def addCompany(data,expected_status_code):
    headers = get_header(universityUsername,password)
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    expected_response_body = ["success", "status", "message", "data"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

def unauthorizedAccess(data):
    response = requests.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

#add valid company data
addCompany(makeData(1000,'haneen','hanen@gmail.com','palestine','1234567','haneen'),200)
#add existing company 
addCompany(makeData(1000,'haneen','hanen@gmail.com','palestine','1234567','haneen'),400)
#add company with invalid email address
addCompany(makeData(543,'haneen','hanen@','palestine','1234567','haneen'),400)
#add company with invalid phone number
addCompany(makeData(569,'haneen','hanen@gmail.com','palestine','1234hs','haneen'),400)
#
unauthorizedAccess(makeData(569,'haneen','hanen@gmail.com','palestine','1234hs','haneen'))

