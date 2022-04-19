import requests
from . import httpbin


class Robot:

    def __init__(self, name, height, color):
        self.url = httpbin
        self.name = name
        self.height = height
        self.color = color
        self.details = "This is " + name + ", of height " + height + " inches" + " and" + " is a " + color

    def intro_self(self):
        return self.name, self.height, self.color


r1 = Robot("Thabang", "7", "Lightskin")
r2 = Robot("Letso", "6", "Druggies")
print(r1.details)
print(r2.details)
print(r1.url)

# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
#
# print(emp_2.fullname())

# def get_ticket(self):
#     URL = '{0} {1}'.format(settings.BASE_URL,
#                            '//REST/1.0/ticket/new?content=Queue: General\n'
#                            'Requestor: guest\n'
#                            'Subject: Test-3221\n'
#                            'Status: new\n'
#                            'Text: class-object-testing')
#     login = {
#         "user": "guest",
#         "pass": "guest"
#     }
#     with requests.Session() as session:
#         post = session.post(URL, data=login)
#         print(post.text)
#     return None

# fail safe me.............................................................#

# @staticmethod
# def fail_safe(self, url, method="POST"):
#     url = 'https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n' \
#           'Requestor: guest\n' \
#           'Subject: Test-3221\n' \
#           'Status: new\n' \
#           'Text: class-object-testing'
#
#     login = {
#         "user": "guest",
#         "pass": "guest"
#     }
#     with requests.Session() as session:
#         post = session.post(url, data=login)
#         print(post.text)
#         return "ticket was created"


# @staticmethod
    # def fail_safe(self, url):
    #     url = 'https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n' \
    #           'Requestor: guest\n' \
    #           'Subject: Test-3221\n' \
    #           'Status: new\n' \
    #           'Text: class-object-testing'
    #
    #     login = {
    #         "user": "guest",
    #         "pass": "guest"
    #     }
    #     with requests.Session() as session:
    #         post = session.post(url, data=login)
    #         print(post.text)
    #         return "ticket was created"
    #

