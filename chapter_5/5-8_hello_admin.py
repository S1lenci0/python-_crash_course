users = ["jose", "enma", "luchy", "admin"]

for user in users:
    if user == "admin":
        print(f"Hello {user}, would you like to se a status report")
    else:
        print(f"Hello {user}, thank you for logging again")