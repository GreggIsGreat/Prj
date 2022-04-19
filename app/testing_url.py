import requests

pt = 'https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n' \
     'Requestor: guest\n' \
     'Subject: Test-3221\n' \
     'Status: new\n' \
     'Text: class-object-testing'

login = {
    "user": "guest",
    "pass": "guest"
}
with requests.Session() as session:
    post = session.post(pt, data=login)
    print(post.text)  # or whatever else you want to do with the request data!
