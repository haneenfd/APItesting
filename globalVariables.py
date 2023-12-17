base_url = 'http://localhost:5000/api/v1'
loginAPI = '/auth/login'
addCompanyAPI = '/company/company'
universityUsername = 'ptuk.en'
password = '123'
jsonScheme = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "status": {"type": "integer"},
        "message": {"type": "string"},
        "data": {
            "type": "object",
            "additionalProperties": True
        }
    },
    "required": ["success", "status", "message"]
}


