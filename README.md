Password Generator (Standard Modules Assignment)

Purpose
This project demonstrates how to use common built-in Python modules to generate two types of passwords:
1) Memorable passwords, made from random words plus digits, joined with hyphens.
2) Random passwords, made from random characters (letters, digits, and optional punctuation).

How it works
When a password is generated, it is appended to a log file along with the day, date, and time it was created.
- Memorable passwords are written to: Memorable/Generated_Passwords.txt
- Random passwords are written to: Random/Generated_Passwords.txt

If the output folders do not exist, the program creates them automatically.

Input requirements
- Download the provided word list file:
  top_english_nouns_lower_100000.txt
- Place it in the same folder as password_generator.py

How to run
1) Open a terminal in the project folder
2) Run:
   python password_generator.py

Menu options
- Memorable password:
  - Choose number of words
  - Choose casing (lower, upper, title, random)

- Random password:
  - Choose password length
  - Choose whether punctuation is included
  - Optionally enter disallowed characters
  

Confirm requirement (generate 1000 passwords)
To confirm folder creation and logging works, the script includes a function that generates 1000 passwords
with the type chosen randomly each time.
- In password_generator.py, uncomment:
  generate_1000_passwords()
- Run the script again. It will append 1000 new entries across both log files.

Modules used
- random
- string
- os / os.path
- time