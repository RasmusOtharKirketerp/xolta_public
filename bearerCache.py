import hashlib
import json
import os
import time
from functools import cache
import xolta_get_auth
import get_config as cred


@cache
def get_auth():
    # check if the token is already cached and has not expired

    input_data = {'username': cred.api_username, 'password': cred.api_password}
    cache_key = hashlib.sha256(json.dumps(input_data).encode()).hexdigest()
    if os.path.exists(f"{cache_key}.txt"):
        with open(f"{cache_key}.txt", "r") as f:
            cached_token = json.load(f)
            print("cached token found!")
        if time.time() < cached_token['expires_at']:
            print("reusing cached token")
            return cached_token['access_token']

    # generate a new token
    print("Generating new token!")
    myXoltaAuth = xolta_get_auth.XoltaBattAuthenticator()
    token = myXoltaAuth.do_login(input_data)

    # cache the token and its expiration time
    expires_at = time.time() + 2 * 60 * 60  # 2 hours
    cached_token = {
        'access_token': token['access_token'], 'expires_at': expires_at}
    with open(f"{cache_key}.txt", "w") as f:
        json.dump(cached_token, f)

    return cached_token['access_token']


def get_auth_with_renewal():
    # check if the token is still valid or has expired
    input_data = {'username': cred.api_username, 'password': cred.api_password}
    cache_key = hashlib.sha256(json.dumps(input_data).encode()).hexdigest()
    if os.path.exists(f"{cache_key}.txt"):
        with open(f"{cache_key}.txt", "r") as f:
            cached_token = json.load(f)
        if time.time() < cached_token['expires_at']:
            return cached_token['access_token']
        else:
            # token has expired, delete the cached token file
            os.remove(f"{cache_key}.txt")

    # generate a new token and cache it
    access_token = get_auth()
    return access_token
