import requests
from globalVariables import base_url, assignTrainerAPI, companyUsername, password
from loginTest import get_header
url = base_url + assignTrainerAPI

def makeData(trainingId,trainerId):
    data = {
        "trainingId": trainingId,
        "trainerId": trainerId,
        }
    return data

def assignTrainer(data,expected_status_code):
    headers = get_header(companyUsername,password)
    response = requests.patch(url, json=data, headers=headers)
    json_data = response.json()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

def unauthorizedAccess(data):
    response = requests.patch(url, json=data)
    json_data = response.json()
    assert response.status_code == 401, f"Expected status code 401 found {response.status_code}"
    expected_response_body = ["success", "status", "message"]
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"

#assign Trainer for accepted training
assignTrainer(makeData(6,1),200)
# edit trainer for running training
assignTrainer(makeData(6,2),200)
# submit invalid  training id
assignTrainer(makeData(1000,1),400)
# submit invalid trainer id
assignTrainer(makeData(1,1000),400)
# missing training id 
assignTrainer({"trainerId":1},500)
#missing trainer id
assignTrainer({"trainingId":6},500)
# unauthrized access
unauthorizedAccess(makeData(6,2))
