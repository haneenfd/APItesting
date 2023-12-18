import requests
from globalVariables import base_url, submitRequestAPI, universityUsername, password
from loginTest import get_header
url = base_url + submitRequestAPI

def makeData(id,type,semester,companyBranchId):
    data = {
        "studentId": id,
        "type": type,
        "semester": semester,
        "companyBranchId": companyBranchId,
        }
    return data

def submitRequest(data,expected_status_code):
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

#submit valid request
submitRequest(makeData(1,"first","summer",1),200)
#submit exist request 
submitRequest(makeData(1,"first","summer",1),400)
#submit invalid  student id
submitRequest(makeData(1000,"first","summer",1),400)
#submit invalid type
submitRequest(makeData(1,"forst","summer",1),400)
#submit invalid semester
submitRequest(makeData(1,"first","sommer",1),400)
#submit nonexistent branch id
submitRequest(makeData(1,"first","summer",1000),400)
#submit second training before first training
submitRequest(makeData(2,"second","summer",1),400)
