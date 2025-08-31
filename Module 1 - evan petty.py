# Simple Authentication and Access Control Example

# Hardcoded users with roles
users = {
    "alice": "admin",
    "bob": "user"
}

# Simulated login
username = input("Enter your username: ")

if username in users:
    role = users[username]
    print(f"Welcome {username}! You are logged in as {role}.")
else:
    print("Invalid user.")
    exit()

# Protected actions
def admin_action():
    print("Admin action: Viewing all system logs.")

def user_action():
    print("User action: Viewing personal dashboard.")

# Access control
if role == "admin":
    admin_action()
elif role == "user":
    user_action()
else:
    print("You do not have access to any actions.")
