# "this is the datatypes in this sheet"
# from numpy.ma.core import append
#
# name = "rahul"
# age = 26
# weight = 60.76
# is_fit = True
#
# print(type(name))
# print(type(age))
# print(type(weight))
# print(type(is_fit))
from pytest_playwright.pytest_playwright import output_path

list1 = [1, 2, 3]
tuple1 = (1,2,3)
set1 = {1,2,3}
dict1 = {
    "name":"rahul",
    "age":26,
    "weight":60.76,
    "is_fit":True,
}

''' these are the examples of list is mutable'''
# list1.append([4,5]) # output is [1,2,3,[4,5]]
# list1.extend([6,7]) # output is [1,2,3,6,7]
# list1.insert(2,8) # output is [1,2,8,3]
# print(list1)

''' immutable and gives this error AttributeError: 'tuple' object has no attribute append'''
# tuple1.append([1,2])

'''I gave the the inputs {1,2,3} and {3,4} its gave me output {1,2,3,4}'''
# set1.update([3,4])
# print(set1)

# dict1["name"] = 'mira'
# # print(dict1)
# dict2 = {
#     "company":"tcs",
#     "ID": 204,
#     "salary": 3000000,
#     }
#
# # dict3 = {**dict1, **dict2}
# dict1.update(dict2)
# dict3 = dict1 | dict2
# print(dict3)#merge two dict

