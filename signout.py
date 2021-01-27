import json
import os

print()
print("Signout")
print()

file = "settings.json"


if os.path.exists(file):
    with open(file, "r") as sign_out_update:
        user_settings = json.load(sign_out_update)

        for settings in user_settings["settings"]:
            for user_preferences in settings["preferences"]:
                for user in user_preferences["user"]:
                    
                    if user["logged_in"]:
                        print("You are now logged out")

                        user["logged_in"] = False
                        user["user_details"] = [{}]
                    
                with open(file, "w") as user_signout:
                    json.dump(user_settings, user_signout, indent=2)