class ServiceRequest:
    "We are going to learn OOPs using GAs utility management system."

    requests = []
    validations = ["High", "Medium", "Low"]

    def __init__(self, request_id, customer_name, priority, status="Pending"):
        self.request_id = request_id
        self.customer_name = customer_name
        self.priority = self.validate_priority(priority)
        self.status = status

    def create_request(self):
        self.reject_duplicate_requests()
        ServiceRequest.requests.append(self.request_id)
        return f"Request {self.request_id} created successfully."

    def validate_priority(self, priority):
        # Capitalize input to match validation list safely (e.g., "high" -> "High")
        formatted_priority = priority.capitalize()
        if formatted_priority not in ServiceRequest.validations:
            raise ValueError("Priority must be one of the following values: High, Medium, Low.")
        return formatted_priority

    def reject_duplicate_requests(self):
        if self.request_id in ServiceRequest.requests:
            raise ValueError(f"Duplicate Request Id: {self.request_id}")

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f"ServiceRequest [ID: {self.request_id}, Customer: {self.customer_name}, Priority: {self.priority}, Status: {self.status}]"

# Testing the code
service_request1 = ServiceRequest(101, 'rahul', 'HIGH', 'In_Progress')
print(service_request1.create_request())
print(service_request1)

# This will raise a ValueError because ID 101 already exists
service_request2 = ServiceRequest(101, 'sonu', 'LOW', 'Pending')
print(service_request2.create_request())