import requests
from globalVariables import base_url, getCompanyTrainersAPI,companyUsername,password
from loginTest import get_header
url = base_url + getCompanyTrainersAPI

def getCompanyTrainers(pageNum,pageSize,expected_status_code):
    response = requests.get(f'{url}?page={pageNum}&size={pageSize}',headers=get_header(companyUsername,password))
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    if expected_status_code == 200:
        expected_response_body = ["items", "pageNumber", "pageSize","totalItems","totalPages"]
    else:
        expected_response_body = ["success", "message", "errors"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"
    if expected_status_code == 200:
        assert len(json_data['items']) <= pageSize, f"Expected {pageSize} items, but got {len(json_data['items'])}"


def unauthorizedAccess():
    response = requests.get(f'{url}?page=0&size=5')
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

#get trainers
getCompanyTrainers(0,6,200)
#get trainers with -ve numbers
getCompanyTrainers(-1,-10,400)
#get company trainers with big numbers
getCompanyTrainers(100,100,200)
#unauthorized access 
unauthorizedAccess()
