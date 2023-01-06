# Hide-folder

This is a simple script to hide a folder in Windows.

## Usage

### Create a `Private` folder

1. Run the command `py hide-folder.py`.
2. The script will be create a new folder in the same directory called `Private`, if it doesn't exist.
3. Put the files you want to hide in the `Private` folder.

### Hide the `Private` folder

1. Run the command `py hide-folder.py` again.
2. The script will hide the `Private` folder.

### Unhide the `Private` folder

1. To unhide the folder, run the command `py hide-folder.py` again.
2. The script will be ask you for the password to unhide the folder.
3. Enter the password and the `Private` folder will be unhidden.

## How to set your own password

1. Open the script with a text editor.
2. Change the value of the variable `master_password` to your own password.

## How to change the name of the folder to hide

1. Open the script with a text editor.
2. Change the value of the variable `folder_name` to your own name.

## How to change the name of the hidden folder

1. Open the script with a text editor.
2. Change the value of the variable `hidden_folder_name` to your own name.