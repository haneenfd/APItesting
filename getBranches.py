import requests
from globalVariables import base_url, getBranchesAPI,universityUsername,password
from loginTest import get_header
url = base_url + getBranchesAPI

def getBranches(data,expected_status_code):
    headers = get_header(universityUsername,password)
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    expected_response_body = ["success", "status", "message", "data"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

def unauthorizedAccess():
    response = requests.post(url, json={"id":1})
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"
#get branches
getBranches({"companyId":1},200)    
#get branches for non existing company 
getBranches({"companyId":10000},400) 
#missing id
getBranches({},500)
#unauthorized access
unauthorizedAccess()