def create_user_database():
    with open("database.txt", "w") as file:
        pass

    while True:
        username = input("Enter a username (or 'q' to quit): ")
        if username.lower() == "q":
            break
        password = input("Enter a password: ")
        
        
        with open("database.txt", "a") as file:
            file.write(f"{username},{password}\n")

def check_user(username, password):
    with open("database.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
    return False

create_user_database()
username = input("Enter your username: ")
password = input("Enter your password: ")
if check_user(username, password):
    print("user exist *_*")
else:
    print(" username or password not found!")
