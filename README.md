Unix Password Cracker
Description

This Python script is designed to perform a dictionary attack on Unix passwords using the information from the /etc/shadow file. It extracts password hashes from the shadow file and compares them against a list of potential passwords from a dictionary file.
Usage

  Make sure to have the necessary permissions to read the /etc/shadow file.
  Prepare a dictionary file (unix_passwords.txt) containing potential passwords, one per line.
  Run the script.
    python unix_password_cracker.py

Example

Consider the following entry in the shadow file:
kali:$y$j9T$7X9YlJ7c4u44URQvzTxxT0$BisyVCLhoPfP22Svis.KFV5tMwCFEJgT7yJIRCHp3G/:19426:0:99999:7:::
The script extracts the salt and iterates through the dictionary file to find a matching password.

Disclaimer

This script is intended for educational and research purposes only. Unauthorized access or use of this script against systems without explicit permission is illegal and unethical.

AUTHOR
<yusufdalbudak>
