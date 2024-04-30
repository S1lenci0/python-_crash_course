users = ["jose", "enma", "luchy", "admin"]
if users:
    for user in users:

        if user == "admin":
            print(f"Hello {user}, would you like to se a status report")
        elif user != "admin":
            print(f"Hello {user}, thank you for logging again")

else:
    print("We need to find some users")

