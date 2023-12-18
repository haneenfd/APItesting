import math
import requests
from globalVariables import base_url, getTrainingRequestsAPI,companyUsername,password
from loginTest import get_header
url = base_url +getTrainingRequestsAPI

def getTrainingRequests(pageNum,pageSize,expected_status_code):
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
        assert len(json_data['items']) <= pageSize or len(json_data['items']) <= 5 , f"Expected {pageSize} items, but got {len(json_data['items'])}"


def unauthorizedAccess():
    response = requests.get(f'{url}?page=0&size=5')
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

#get Training Requests
getTrainingRequests(0,6,200)
#get Training Requests -ve numbers
getTrainingRequests(-1,-10,400)
#get Training Requests with big numbers
getTrainingRequests(100,100,200)
#get Training Requests with null values
getTrainingRequests(math.nan,math.nan,400)
#unauthorized access 
unauthorizedAccess()
