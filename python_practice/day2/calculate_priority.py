requests = [
    {"id": 101, "priority": "LOW"},
    {"id": 102, "priority": "HIGH"},
    {"id": 103, "priority": "MEDIUM"},
]

def calculate_priority(priority):
    if priority == "HIGH":
        return 1
    elif priority == "MEDIUM":
        return 2
    elif priority == "LOW":
        return 3
    else:
        raise ValueError("Invalid priority")

sorted_requests = sorted(requests, key=lambda request: calculate_priority(request["priority"]))
for request in sorted_requests:
    print(
        request["id"],
        "→",
        request["priority"]
    )


