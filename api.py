##############################################################################
#                                                                            #
# This file handles calls to Cobalt over different REST types (Put, Get etc) #
#                                                                            #
##############################################################################

import requests

BASE_URL = "https://test.myabf.com.au"
BASE_URL = "http://127.0.0.1:8000"


class CallType:
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"


def cobalt_api_call_post(cobalt_api_key, path, payload):
    """ Process a POST request """

    return _cobalt_api_call(CallType.POST, cobalt_api_key, path, payload)


def cobalt_api_call_get(cobalt_api_key, path, payload):
    """ Process a GET request """

    return _cobalt_api_call(CallType.GET, cobalt_api_key, path, payload)


def cobalt_api_call_put(cobalt_api_key, path, payload):
    """ Process a PUT request """

    return _cobalt_api_call(CallType.PUT, cobalt_api_key, path, payload)


def cobalt_api_call_delete(cobalt_api_key, path, payload):
    """ Process a DELETE request """

    return _cobalt_api_call(CallType.DELETE, cobalt_api_key, path, payload)


def _cobalt_api_call(call_type, cobalt_api_key, path, payload):
    """ Calls cobalt API and returns status and any response as a python object """

    api_url = f"{BASE_URL}/{path}"

    if call_type == CallType.POST:
        response = requests.post(api_url, json=payload, headers={"key": cobalt_api_key})
    elif call_type == CallType.GET:
        response = requests.get(api_url, json=payload, headers={"key": cobalt_api_key})
    elif call_type == CallType.PUT:
        response = requests.put(api_url, json=payload, headers={"key": cobalt_api_key})
    elif call_type == CallType.DELETE:
        response = requests.delete(api_url, json=payload, headers={"key": cobalt_api_key})
    else:
        raise AttributeError(f"Invalid call type: {call_type}")

    return response.status_code, response.json()
