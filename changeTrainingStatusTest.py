import requests
from globalVariables import base_url, changeTrainingStatusAPI, companyUsername, password
from loginTest import get_header
url = base_url + changeTrainingStatusAPI

def makeData(trainingId,status):
    data = {
        "trainingId": trainingId,
        "status": status,
        }
    return data

def changeTrainingStatus(data,expected_status_code):
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
changeTrainingStatus(makeData(1,"accepted"),200)
# submit invalid  training id
changeTrainingStatus(makeData(1000,"running"),400)
# submit invalid status
changeTrainingStatus(makeData(1,"ruenning"),400)
# missing training id 
changeTrainingStatus({"status":"running"},500)
#missing status
changeTrainingStatus({"trainingId":4},500)
# unauthrized access
unauthorizedAccess(makeData(1,"accepted"))
