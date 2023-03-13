import requests
import json
import bearerCache as b
import get_config as cred


def get_data():
    url = "https://external.xolta.com/api/GetDataSummary"
    params = {
        "DeviceId": cred.api_deviceid,
        "SiteId": cred.api_siteid,
        "last": "3000",
        "IsBlob": "false",
        "CalculateConsumptionNeeded": "false",
        "resolutionMin": "10",
        "fromDateTime": "2023-02-16"
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + b.get_auth_with_renewal()
    }

    response = requests.get(url, params=params, headers=headers)
    data = json.loads(response.text)
    # print(data)
    return data["telemetry"]
