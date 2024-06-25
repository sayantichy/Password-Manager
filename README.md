# Password-Manager🔐
Simple Password Manager: A basic password manager built with Python, utilizing the 'cryptography.fernet' module for secure password encryption and decryption.
## Features✨
- Add New Passwords: Securely add new usernames and passwords, which are encrypted before being saved.🔒
- View Existing Passwords: Decrypt and display stored passwords for easy retrieval.🔓
- Secure Storage: All passwords are stored in an encrypted format, ensuring your data remains protected.🛡️
## Setup🛠️
- Prerequisites📋
Python 3.x🐍
cryptography library🔐
### Install the required library using pip:

- pip install cryptography
Initial Key Generation🔑
Generate a new encryption key (only needed once):

#### Uncomment the write_key() line in the script.
Run the script to generate the key.

### Uncomment the following line if you need to generate a new key
### write_key()
Comment out or remove the write_key() line to prevent overwriting the key in future runs.
## Usage🚀
- Run the Script:
python password_manager.py
- Choose an Option:
- Type add to add a new password.
- Type view to view existing passwords.
- Type q to quit the program.
## How It Works⚙️
- Encryption: When adding a new password, the script encrypts it using the Fernet symmetric encryption algorithm before storing it in password_manager.txt.🔐
- Decryption: When viewing passwords, the script decrypts the stored passwords to display them in plain text.🔓
