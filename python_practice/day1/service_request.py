requests = []

def create_request():
    title = input("Enter title: ")
    priority = input("Enter priority: ")


    request={
        "title": title,
        "priority": priority,
        "status": "Completed",
    }

    requests.append(request)
    print("Request Created Successfully")

def view_requests():
    if  not requests:
        print("Request not found")
        return
    for request in requests:
        print(request)


def delete_request():
    deleted = False

    for request in requests.copy():
        if request["status"] == "Completed":
            requests.remove(request)
            deleted = True

    if not deleted:
        print("Completed Request not found")
    else:
        print("Completed Requests deleted successfully")

while True:
    print("\n1. Create Request ")
    print("2. View Requests")
    print("3. Delete Request")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        create_request()
    elif choice == "2":
        view_requests()
    elif choice == "3":
        delete_request()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")