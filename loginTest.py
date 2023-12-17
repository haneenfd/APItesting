import requests
import json
from globalVariables import base_url, loginAPI
url = base_url + loginAPI
def valid_login_test():
    data = {
        "username": "ptuk.en",
        "password":"123"
    }
    expected_response_body = ["success", "status", "message", "data", "accessToken"]
    response = requests.post(url, json=data)
    json_data = response.json()
    for key in expected_response_body:
        assert key in json_data, f"Expected key '{key}' in the response body"
    access_token = json_data["accessToken"]
    assert access_token, "Access token should not be empty"
    assert response.status_code == 200

def invalid_username_test():
    data = {
        "username": "hajar",
        "password":"123"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 401

def invalid_password_test():
    data = {
        "username": "ptuk.en",
        "password":"124"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 401

def missing_attribute_test():
    data = [{
        "password":"124"
    },{
        "username": "ptuk.en"
    }]
    for entry in data:
        response = requests.post(url, json=entry)
        assert response.status_code == 500

def get_header(username, password):
    data = {
        "username": username,
        "password":password
    }
    response = requests.post(url, json=data)
    json_data = response.json()
    access_token = json_data["accessToken"]
    headers = {'access-token': access_token}
    return headers

valid_login_test()
invalid_username_test()
invalid_password_test
missing_attribute_test()