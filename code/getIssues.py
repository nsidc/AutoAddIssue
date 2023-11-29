import requests
import bs4
import json

# Function to simplify the process of making python requests
# returns None if the request is unsuccessful
def make_request(URL, data, headers):
# ****************************************************
# Use of try and exception handeling provided by GeeksForGeeks at https://www.geeksforgeeks.org/exception-handling-of-python-requests-module/
    r = None
    try:
        r = requests.get(URL, params=json.dumps(data), headers=headers, timeout=5)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
        return None
    except requests.exceptions.ReadTimeout as errrt:
        print("Time out")
        return None
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
        return None
    except requests.exceptions.RequestException as errex:
        print("Exception request")
        print(errex.args[0])
        return None
    return r


# Will get a list of all the issues currently stored in a repository and print them out
# Will return None if unsuccessful, and a list if successful
def get_issue(REPO_NAME, PAT):
    URL = f'https://api.github.com/repos/{REPO_NAME}/issues'

    headers = {
        'Authorization': 'token ' + PAT
    }

    data = { 'state': 'open' }

    r = make_request(URL, data, headers)

    if r is None:
        return None
    
    if r.ok:
        print(type(r.json()))


# For testing the functions above

# Testing getting all of the issues of this repository
PAT = ""
REPO_NAME = "nsidc/AutoAddIssue"
OWNER_NAME = "IanSinColorado"
get_issue(REPO_NAME, PAT)