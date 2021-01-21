import json
import os

print()
print("login")
print()

username = input("Please enter your username: ")
uuid = input("Please enter your UUID: ")


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
                            default_user_settings = [{"username": user_name, "email": user_email}]
                            user["user_settings"] = default_user_settings

                    with open("settings.json", "w") as user_defaults:
                        json.dump(user_settings, user_defaults, indent=2)


if os.path.exists(f"{username}_{uuid}.json"):
    with open(f"{username}_{uuid}.json", "r") as read_data:
        data = json.load(read_data)

    for username_data in data["user"]:
        if username_data["username"] != username:
            print()
            print("You json file seems to not have that data within it")
            print(
                "Possible Problems: The file could be corrupt. The object username does not exist or has the wrong value")
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
