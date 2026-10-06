"""Arithmetic"""

# a = 20
# b = 5
# print(a + b) # addition
# print(a - b )#substrction
# print(a * b) #multiplication
# print(a/b)  # division
# print(a // b)#floor division
# print(a % b)  # moduler
# print(a ** b) #power

"""Comparison"""
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

"""Logical"""
# age = 20
# is_activate = True
# if age >= 18 and is_activate:
#     print("Allowed")

"""Conditions"""
# status = "PENDING"
# if status == "PENDING":
#     print("Status is PENDING")
# elif status == "IN_PROGRESS":
#     print("Status is IN PROGRESS")
# elif status == "COMPLETED":
#     print("Status is COMPLETED")
# else:
#     print("Status is UNKNOWN")

"""Loops"""
# reqts = ["REQ001","REQ002","REQ003"]
# for req in reqts:
#     print(req)
#
# while reqts:
#     print(reqts.pop())

"""break"""
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
#
# for i in range(10):
#     if i <= 5:
#         continue
#     print(i)

# for i in range(10):
#     if i == 3:
#         continue
#     if i == 7:
#         break
#     print(i)
# '''lists'''
# requests = [
#     "Gas leakage",
#     "New connection",
#     "Meter issue"
# ]
#
# print(requests[0])
#
# requests.append("Billing issue")
# print(requests)
#
# requests.insert(0,'Emergency request')
# print(requests)
# requests.remove("Meter issue")
# print(requests)
# requests.pop()
# print(requests)

# """dictionary"""
# request = {
#     "id": 101,
#     "customer": "Shubhashri",
#     "priority": "HIGH",
#     "status": "PENDING"
# }
#
# print(request["customer"])
# print(request.get("customer"))
#
# request["status"] = "IN_PROGRESS"
# # print(request)
#
# for key, value in request.items():
#     print(key, value)

"""functions"""
# def calculate_priority(priority):
#     if priority == 'HIGH':
#         return 1
#     return 2
#
# print(calculate_priority("HIGH"))
