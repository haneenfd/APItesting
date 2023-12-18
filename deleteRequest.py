import requests
from globalVariables import base_url, deleteRequestAPI,universityUsername,password
from loginTest import get_header
import math

url = base_url + deleteRequestAPI

def deleteRequest(id,expected_status_code):
    headers = get_header(universityUsername,password)
    response = requests.delete(f'{url}{id}',headers=headers)
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

def unauthorizedAccess():
    response = requests.delete(f'{url}1')
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code {401} found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"
#delete training request
deleteRequest(9,200)
#delete non existing id
deleteRequest(9,200)
#delete without send id
deleteRequest(math.nan,500)
#unauthorized delete
unauthorizedAccess()