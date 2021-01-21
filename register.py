from datetime import datetime
import random
import json
import os

print()
print("Sign Up Form")
print()


def user_login_func():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as settings_update:
            user_settings = json.load(settings_update)

            for settings in user_settings["settings"]:
                for user_preferences in settings["preferences"]:
                    for user in user_preferences["user"]:

                        if user["logged_in"]:
                            print("You are already logged in")
                            exit()
                        else:
                            user["logged_in"] = True

                    with open("settings.json", "w") as user_login:
                        json.dump(user_settings, user_login, indent=2)

                        if user["logged_in"]:
                            default_user_settings = [{"username": user_name, "email": email}]
                            user["user_details"] = default_user_settings

                    with open("settings.json", "w") as user_defaults:
                        json.dump(user_settings, user_defaults, indent=2)


if os.path.exists("settings.json"):
    with open("settings.json", "r") as settings_update:
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

                        # Simple requirements for UserName and Email
                        if len(user_name) < 3:
                            print()
                            user_name = input("You need to enter a username:  ")

                            if len(user_name) < 3:
                                print()
                                print("You have failed the login process, please try again.")
                                exit()

                            elif len(user_name) > 3:
                                email = input("Please enter a email:  ")

                                if len(email) < 3:
                                    print()
                                    print("You have failed the login process, please try again.")
                                    exit()

                                elif len(email) > 3:
                                    # Creates a file for The user using the username and the uuid,
                                    # e.g. user_106033536.json
                                    dataFile = open(f"{user_name}_{uuid}.json", "w")

                                    # User data formatting for json
                                    data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\"" + "}]" + "}"

                                    # Writes the data into the .json file
                                    dataFile.write(str(data))
                                    dataFile.close()

                                    print()
                                    print(
                                        f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
                                    print(
                                        f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
                                    print()

                                    file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
                                    print(
                                        "Your data has been saved: " + file_path)  # Prints where the data has been saved

                                    exit()

                        else:
                            email = input("Please enter a email: ")
                            if len(email) < 3:
                                print()
                                email = input("You need to enter a email:  ")

                                if len(email) < 3:
                                    print()
                                    print("You have failed the login process, please try again.")
                                    exit()

                                elif len(email) > 3:
                                    # Creates a file for The user using the username and the uuid,
                                    # e.g. user_106033536.json
                                    dataFile = open(f"{user_name}_{uuid}.json", "w")

                                    # User data formatting for json
                                    data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\"" + "}]" + "}"

                                    # Writes the data into the .json file
                                    dataFile.write(str(data))
                                    dataFile.close()

                                    user_login_func()

                                    print()
                                    print(
                                        f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
                                    print(
                                        f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
                                    print()

                                    file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
                                    print(
                                        "Your data has been saved: " + file_path)  # Prints where the data has been saved

                                    exit()

                            # Creates a file for The user using the username and the uuid,
                            # e.g. user_106033536.json
                            dataFile = open(f"{user_name}_{uuid}.json", "w")

                            # User data formatting for json
                            data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\"" + "}]" + "}"

                            # Writes the data into the .json file
                            dataFile.write(str(data))
                            dataFile.close()

                            user_login_func()

                        print()
                        print(f"Your information has been saved in {user_name}_{uuid}.json")  # Tells you your file name
                        print(
                            f"Make sure to remember this uuid, you will need it later, {uuid}")  # Links you to your file directory
                        print()

                        file_path = os.path.abspath(f'{user_name}_{uuid}.json')  # File path
                        print("Your data has been saved: " + file_path)  # Prints where the data has been saved
