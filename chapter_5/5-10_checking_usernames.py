current_users = ["jose", "enma", "luchy", "admin"]
new_users = ["jose", "maria"]

for user in new_users:
    if user in current_users:
        print(f"{user} is not available. Please choose a another username.")
    else:
        print(f"{user} is available")