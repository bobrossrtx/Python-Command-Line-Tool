# noinspection PyInterpreter
from datetime import datetime
from getpass import getpass
import hashlib
import random
import json
import os

print()
print("Sign Up Form")
print()

file = "settings.json"
failed = 'You have failed the login process, please try again.'

valid_email = "@" + "."
valid_email_error= "you need to enter a valid email address"

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

                    with open(file, "w") as user_login:
                        json.dump(user_settings, user_login, indent=2)

                        if user["logged_in"]:
                            default_user_details = [{"username": user_name, "email": email}]
                            user["user_details"] = default_user_details

                    with open(file, "w") as user_defaults:
                        json.dump(user_settings, user_defaults, indent=2)

def password():
    password = getpass("Please enter a password: ")

    if len(password) < 8:
        print("you're password must be longer than 8 chars")
        password = getpass("Please re-enter your password: ")

        if len(password) > 8:
            if "(" or ")" or "{" or "}" or "[" or "]" or "{" or "}" or "|" or "\\" in password:
                print("you're password must not have any bracket chars")
                password = getpass("Please re-enter your password: ")
            else:
                if "!" or "#" or "$" or "&" or "*" or "+" or "=" or "-" or "_" or "@" or "<" or ">" in password:
                    # Creates a file for The user using the username and the uuid,
                    # e.g. user_106033536.json
                    data_file = open(f"{user_name}_{uuid}.json", "w")

                    password_e = bytes(password, "utf-8")
                    
                    password_h = hashlib.sha256(password_e)
                    password_s = password_h.hexdigest()

                    # User data formatting for json
                    data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\",\"password\": \"{password_s}\", \"settings\": [" + "{" + "\"password\": false}]}]}"

                    # Writes the data into the .json file
                    data_file.write(str(data))
                    data_file.close()

                    print()
                    print(
                        f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
                    print(
                        f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
                    print()

                    file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
                    print(saved_data + file_path)  # Prints where the data has been saved

                    user_login_func()

                    exit()

    elif "!" or "#" or "$" or "&" or "*" or "+" or "=" or "-" or "_" or "@" or "<" or ">" and "q" or "w" or "e" or "r" or "t" or "y" or "u" or "i" or "o" or "p" or "a" or "s" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "z" or "x" or "c" or "v" or "b" or "n" or "m"  in password:
        # Creates a file for The user using the username and the uuid,
        # e.g. user_106033536.json
        data_file = open(f"{user_name}_{uuid}.json", "w")

        password_e = bytes(password, "utf-8")
                    
        password_h = hashlib.sha256(password_e)
        password_s = password_h.hexdigest()

        # User data formatting for json
        data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\",\"password\": \"{password_s}\", \"settings\": [" + "{" + "\"password\": false}]}]}"

        # Writes the data into the .json file
        data_file.write(str(data))
        data_file.close()

        print()
        print(
            f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
        print(
            f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
        print()

        file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
        print(saved_data + file_path)  # Prints where the data has been saved

        user_login_func()

        exit()

    elif "(" or ")" or "{" or "}" or "[" or "]" or "{" or "}" or "|" or "\\" in password:
        print("you're password must not have any bracket chars")
        password = getpass("Please re-enter your password: ")

    else:
        # Creates a file for The user using the username and the uuid,
        # e.g. user_106033536.json
        data_file = open(f"{user_name}_{uuid}.json", "w")

        password_e = bytes(password, "utf-8")
                    
        password_h = hashlib.sha256(password_e)
        password_s = password_h.hexdigest()

        # User data formatting for json
        data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\",\"password\": \"{password_s}\", \"settings\": [" + "{" + "\"password\": false}]}]}"

        # Writes the data into the .json file
        data_file.write(str(data))
        data_file.close()

        print()
        print(
            f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
        print(
            f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
        print()

        file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
        print(saved_data + file_path)  # Prints where the data has been saved

        user_login_func()

        exit()


if os.path.exists(file):
    with open(file, "r") as settings_update:
        user_settings = json.load(settings_update)

        for settings in user_settings["settings"]:
            for user_preferences in settings["preferences"]:
                for user in user_preferences["user"]:
                    if user["logged_in"]:
                        print("You already logged in. You cannot make a new account while logged in")
                    else:
                        dt = datetime(2018, 1, 1)
                        seed = int(round(dt.timestamp() * 10))
                        start_number = random.randint(1, 10)
                        uuid = round(start_number * seed / 1000)  # Creates the uuid variable from a random number

                        user_name = input("Please enter a username: ")
                        saved_data = "Your data has been saved: "

                        # Simple requirements for UserName and Email
                        if len(user_name) < 3:
                            print()
                            user_name = input("You need to enter a username:  ")


                            if len(user_name) < 3:
                                print()
                                print(failed)
                                exit()

                            elif len(user_name) > 3:
                                email = input("Please enter a email:  ")

                                if len(email) < 3:
                                    print()
                                    print(failed)
                                    exit()

                                elif len(email) > 3:
                                    if valid_email in email:
                                        password()
                                    else:
                                        print(valid_email_error)

                        else:
                            email = input("Please enter a email: ")
                            if len(email) < 3:
                                print()
                                email = input("You need to enter a email:  ")

                                if len(email) < 3:
                                    print()
                                    print(failed)
                                    exit()

                                elif len(email) > 3:
                                    if valid_email in email:
                                        password()
                                    else:
                                        print(valid_email_error)

                            else:
                                password()

                        print()
                        print(f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
                        print(
                            f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
                        print()

                        file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
                        print(saved_data + file_path)  # Prints where the data has been saved
