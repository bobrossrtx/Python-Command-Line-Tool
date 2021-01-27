import json
import os
from getpass import getpass
import hashlib

print()
print("login")
print()

file = "settings.json"

def already_logged_in():
    with open(file, "r") as settings_update:
        user_settings = json.load(settings_update)

        for settings in user_settings["settings"]:
            for user_preferences in settings["preferences"]:
                for user in user_preferences["user"]:

                    if user["logged_in"]:
                        print("You are already logged in")
                        exit()

def user_login_func():
    if os.path.exists(file):
        with open(file, "r") as settings_update:
            user_settings = json.load(settings_update)

            for settings in user_settings["settings"]:
                for user_preferences in settings["preferences"]:
                    for user in user_preferences["user"]:

                        if user["logged_in"]:
                            print("You are already logged in")
                            exit()
                        else:
                            user["logged_in"] = True
                            default_user_details = [{"username": user_name, "email": user_email}]
                            user["user_details"] = default_user_details

                    with open(file, "w") as user_login:
                        json.dump(user_settings, user_login, indent=2)

already_logged_in()


username = input("Please enter your Username: ")
uuid = input("Please enter your UUID: ")

if os.path.exists(file):
    with open(f"{username}_{uuid}.json", "r") as settings_update:
        user = json.load(settings_update)

        for settings in user["user"]:
            if settings["password"]:
                if os.path.exists(f"{username}_{uuid}.json"):
                    with open(f"{username}_{uuid}.json", "r") as read_data:
                        data = json.load(read_data)

                        for settings in data["user"]:
                            for password_login in settings["settings"]:
                                if password_login["password"]:
                                    password = getpass("Please enter your Password: ")

                                    password_e = bytes(password, "utf-8")
                    
                                    password_h = hashlib.sha256(password_e)
                    
                                    password_s = password_h.hexdigest()

                                    for username_data in data["user"]:
                                        if username_data["username"] != username or username_data["uuid"] != uuid or username_data["password"] != password_s:
                                            print()
                                            print("That json file seems to not have that data within it")
                                            print(f"Possible Problems: The file could be corrupt. The object {username}, {uuid} or {password} does not exist or has the wrong value")
                                        else:
                                            user_name = username_data["username"]
                                            user_uuid = username_data["uuid"]
                                            user_email = username_data["email"]
                                            print()
                                            print(f"You are now logged in as {user_name}")
                                            print()
                                            print(f"Your uuid: {user_uuid}")
                                            print(f"Your email: {user_email}")
                                            print()

                                            with open(file, "r") as settings_update:
                                                user_details = json.load(settings_update)

                                    user_login_func()

                elif username or uuid or password == "":
                    print("You need to enter the correct username and uuid")
                    print()
                    print("Please try again")
            else:
                if os.path.exists(f"{username}_{uuid}.json"):
                    with open(f"{username}_{uuid}.json", "r") as read_data:
                        data = json.load(read_data)

                    for username_data in data["user"]:
                        if username_data["username"] != username  or username_data["uuid"] != uuid:
                            print()
                            print("You json file seems to not have that data within it")
                            print("Possible Problems: The file could be corrupt. The object username does not exist or has the wrong value")
                        else:
                            user_name = username_data["username"]
                            user_uuid = username_data["uuid"]
                            user_email = username_data["email"]
                            print()
                            print(f"You are now logged in as {user_name}")
                            print()
                            print(f"Your uuid: {user_uuid}")
                            print(f"Your email: {user_email}")
                            print()

                    user_login_func()

                elif username or uuid == "":
                    print("You need to enter the correct username and uuid")
                    print()
                    print("Please try again")
