import requests

parameters = {
    "user": "guest",
    "pass": "guest"}
response = requests.post('https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n''Requestor: '
                         'guest\n''Subject: Test-3221\n''Status: new\n''Text: class-object-testing', params=parameters)
print(response.text)
