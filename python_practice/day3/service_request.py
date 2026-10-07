class ServiceRequest:
    def __init__(self, name, request_id,priority,status, ):
        self.name = name
        self.request_id = request_id
        self.priority = priority
        self.status = status

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f"name:{self.name}, request_id:{self.request_id}, priority:{self.priority}, status:{self.status}"

new_request = ServiceRequest("rahul","234",'LOW',"Pending")
new_request.update_status("In Progress")
print(new_request)