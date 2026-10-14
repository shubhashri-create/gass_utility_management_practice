# class Customer:
#     def __init__(self,name,phone):
#         self.name=name
#         self.phone=phone
#
#
#     def display(self):
#         print("Name:", self.name)
#         print("Phone:", self.phone)
#
#
#
# customer1 = Customer("shubhashri","0983024874")
# customer2 = Customer("dhanshri","1234587690")
#
# customer1.display()
# customer2.display()
#
# class Engineer:
#     def __init__(self,name,place,id):
#         self.name=name
#         self.place=place
#         self.id=id
#
#     def __str__(self):
#         return f"name:{self.name} \nplace:{self.place} \nid:{self.id}"
#
# engineer1 = Engineer("maroti","pune",2)
# print(engineer1)

# class ServiceRequest:
#
#     def __init__(self, request_id, customer, priority, status):
#         self.request_id = request_id
#         self.customer = customer
#         self.priority = priority
#         self.status = status
#
#     def display(self):
#         print("request_id:", self.request_id)
#         print("customer:", self.customer)
#         print("priority:", self.priority)
#         print("status:", self.status)
#
# request1 = ServiceRequest(101, "Rahul", "HIGH", "Pending")
# request2 = ServiceRequest(102, "Priya", "LOW", "In Progress")
#
# request1.display()
# request2.display()

# class ServiceRequest:
#     def __init__(self,request_id,status):
#         self.request_id = request_id
#         self.status = status
#
#     def update_status(self, new_status):
#         self.status = new_status
#
#     def display(self):
#         print(self.request_id)
#         print(self.status)
#
# request = ServiceRequest(101, "Pending")
# request.display()
# request.update_status("In_progress")
# request.display()

# class User:
#     def get_rol(self):
#         print("general user")
#
#
# class Engineer(User):
#    def get_rol(self):
#        print("engineer")
#
# user = User()
# engineer= Engineer()
# user.get_rol()
# engineer.get_rol()

# class Customer():
#       def __init__(self, name, password):
#           self.name = name
#           self.__password = password
#
#       def change_password(self, new_password):
#           self.__password = new_password
#
#       def get_password(self):
#           return self.__password
#
# customer = Customer("rahul","1234567")
# print(customer.name)
# customer.change_password(new_password="9877654")
# print(customer.get_password())


# from abc import ABC, abstractmethod
#
# class Notification(ABC):
#
#      @abstractmethod
#      def send(self):
#          pass
#
# class SMSNotification(Notification):
#      def send(self):
#          print("SMS")
#
# class EmailNotification(Notification):
#     def send(self):
#         print("Email")
#
# sms = SMSNotification()
# sms.send()
# email = EmailNotification()
# email.send()
#
# notifications = [SMSNotification(),EmailNotification()]
# for notification in notifications:
#     notification.send()
#
# class Customer:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class ServiceRequest:
#
#     def __init__(self, request_id, customer):
#         self.request_id = request_id
#         self.customer = customer
#
#
# customer = Customer("Rahul")
#
# request = ServiceRequest(101, customer)
#
# print(request.request_id)
# print(request.customer.name)

class User():
    """This th class we are using to have login credentials"""
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def login(self):
        print("Login successful")

class Customer(User):
    """This class is using to have Customers data"""
    def __init__(self, name,email, phone, request_id, priority, status):
        super().__init__(name,email)
        self.phone = phone
        self.request_id = request_id
        self.priority = priority
        self.status = status


class Engineer(User):
    """This class is using to have Engineers data"""
    def __init__(self, name,email, phone, speciality):
        super().__init__(name,email)
        self.phone = phone
        self.speciality = speciality

engineers = Engineer("maroti","abc@gmail.com",74368634543,"HP")
customers = Customer("ganraj","abc@gmmail.com",74368464369,123,"HIGH","PENDING")

print(customer.name)
print(customer.email)
print(customer.phone)

print(engineer.name)
print(engineer.email)
print(engineer.speciality)

customer.login()
engineer.login()


