import requests
from globalVariables import base_url, addBranchAPI,universityUsername,password
from loginTest import get_header
url = base_url + addBranchAPI

def makeData(id,location):
    data = {
        "id": id,
        "location": location,
        }
    return data

def addBranch(data,expected_status_code):
    headers = get_header(universityUsername,password)
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"


def unauthorizedAccess(data):
    response = requests.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"


#add branch
addBranch(makeData(1,'jordan'),200)
#add existing branch 
addBranch(makeData(1,'jordan'),200)
#add branch for non existing company 
addBranch(makeData(10000,'jordan'),400)
#unauthorized action
unauthorizedAccess(makeData(1,'jordan'))
#missing id attribute
addBranch({"branch":"nablus"},500)
# missing branch attribute
addBranch({"id":1},500)