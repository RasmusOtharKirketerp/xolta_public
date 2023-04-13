import requests
import json
import bearerCache as b
import get_config as cred


from datetime import datetime, timedelta
import json
import requests


def get_data():
    url = "https://external.xolta.com/api/GetDataSummary"

    # calculate the date 10 days ago
    ten_days_ago = datetime.now() - timedelta(days=10)
    formatted_date = ten_days_ago.strftime("%Y-%m-%d")

    params = {
        "DeviceId": cred.api_deviceid,
        "SiteId": cred.api_siteid,
        "last": "3000",
        "IsBlob": "false",
        "CalculateConsumptionNeeded": "false",
        "resolutionMin": "10",
        "fromDateTime": formatted_date
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + b.get_auth_with_renewal()
    }

    response = requests.get(url, params=params, headers=headers)
    data = json.loads(response.text)
    # print(data)
    return data["telemetry"]
