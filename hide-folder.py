import os
import getpass

master_password = "YOUR_PASSWORD_HERE"
folder_name = "Private" # Name of the folder to lock
hidden_folder_name = "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" # The script will rename the folder to this name

def lock_folder():
    # Rename the folder and set system and hidden attributes
    os.rename(folder_name, hidden_folder_name)
    os.system("attrib +h +s \""+hidden_folder_name+"\"")
    print("Folder locked")

def unlock_folder():
    # Prompt for password
    password = getpass.getpass("Enter password to unlock folder: ")

    if password == master_password:
        # Remove system and hidden attributes and rename the folder back
        os.system("attrib -h -s \""+hidden_folder_name+"\"")
        os.rename(hidden_folder_name, folder_name)
        print("Folder unlocked successfully")
    else:
        print("Invalid password")

# Check if the user is an administrator
if os.path.exists(hidden_folder_name):
    unlock_folder()
else:
    # Check if the folder exists
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("Private folder created successfully")
    else:
        # Prompt user to confirm they want to lock the folder
        answer = input("Are you sure you want to lock the folder? (Y/N) ")
        if answer.lower() == "y":
            lock_folder()
        else:
            print("Operation cancelled")
