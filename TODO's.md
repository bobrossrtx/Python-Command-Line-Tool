- [x] add after password:
```python
# Creates a file for The user using the username and the uuid,
# e.g. user_106033536.json
dataFile = open(f"{user_name}_{uuid}.json", "w")

# # User data formatting for json
data = "{\"user\":[{" + f"\"username\": \"{user_name}\", \"email\": \"{email}\", \"uuid\": \"{uuid}\", \"settings\": [" + "{" + "\"password\": false}]}]}"

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
print(saved_data + file_path)  # Prints where the data has been saved

exit()
```