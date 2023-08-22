import csv
import json

compromised_users = []

# GETTING LIST OF COMPROMISED USERS
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)

  for password_row in password_csv:
    compromised_users.append(password_row["Username"])

# ADDING LIST OF COMPROMISED USERS TO FILE
with open("compromised_users.txt", 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user + "\n")

# USING JSON MODULE TO CREATE A JSON FILE
with open("boss_message.json", 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)
