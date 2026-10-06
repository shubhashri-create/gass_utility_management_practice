# age  = "25"+2
# print(age)# this gave us error because the string and int cannot be added we have do type casting here
age = 25
age = int(age)+ 2 # here we converted string in int using int(age)
print(age)