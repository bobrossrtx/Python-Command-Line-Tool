import json
import os

if os.path.exists("settings.json"):
    with open("settings.json", "r") as sign_out_update:
        user_settings = json.load(sign_out_update)

        for settings in user_settings["settings"]:
            for user_preferences in settings["preferences"]:
                for user in user_preferences["user"]:
                    
                    if user["logged_in"]:
                        print("You are now logged out")

                        user["logged_in"] = False
                    
                with open("settings.json", "w") as user_signout:
                    json.dump(user_settings, user_signout, indent=2)