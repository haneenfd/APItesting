import requests
from globalVariables import base_url, getCompanyFieldsAPI,companyUsername,password
from loginTest import get_header
url = base_url + getCompanyFieldsAPI

def getCompanyFields():
    headers = get_header(companyUsername,password)
    response = requests.get(url, headers=headers)
    json_data = response.json()
    assert response.status_code == 200, f"Expected status code 200 found {response.status_code}"
    expected_response_body = ["success", "status", "message", "data"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

def unauthorizedAccess():
    response = requests.get(url)
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"
#get branches
getCompanyFields()    
#unauthorized access
unauthorizedAccess()