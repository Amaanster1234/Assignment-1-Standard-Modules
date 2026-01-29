import os
import random
import string
import time

#-----------------------------------------------------
#Helpers
#-----------------------------------------------------
def ensure_dirs():
    #Create output directories if they don't exist.
    if not os.path.exists("Memorable"):
        os.mkdir("Memorable")
    if not os.path.exists("Random"):
        os.mkdir("Random")

def timestamp_str():
    #Return a readable timestamp including day, date,and time.
    return time.ctime()

def append_to_file(folder, password):
    #Append password and timestamp to the correct Generated_Passwords.txt file.
    ensure_dirs()
    filename = os.path.join(folder, "Generated_Password.txt")
    with open(filename, "a") as file:
        file.write(timestamp_str() + " | " + password + "\n")
   

def load_words(filepath):
    #Load words (one per line) from the provided nouns file.
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            "Missing word file: " + filepath + "\n"
            "Download top_english_nouns_lower_100000.txt and place it in the project folder."
        )
    words = []
    with open(filepath, "r") as file:
        for line in file:
            w = line.strip()
            if w != "":
                words.append(w)
    if len(words) == 0:
        raise ValueError("Word list file is empty")
    return words

def apply_case(word, case_option):
    #Apply chosen casing to a word.
    case_option = case_option.lower()

    if case_option == "lower":
        return word.lower()
    if case_option == "upper":
        return word.upper()
    if case_option == "title":
        return word.title()
    if case_option == "random":
        return random.choice([word.lower(), word.upper(), word.title()])
    
    raise ValueError("case_option must be: lower, upper, title, or random")

#-------------------------
#Memorable Password
#-------------------------
def generate_memorable_password(words, n_words, case_option):
    if n_words < 1:
        raise ValueError("n_words must be >= 1")
    
    if n_words <= len(words):
        chosen = random.sample(words, n_words)
    else:
        chosen = [random.choice(words) for i in range(n_words)]

    parts = []
    for w in chosen:
        w2 = apply_case(w, case_option)
        digit = str(random.randint(0,9))
        parts.append(w2 + digit)
    
    return "-".join(parts)

#--------------------------
#Random Password
#--------------------------
def generate_random_password(length, include_punctuation, disallowed):
    if length < 1:
        raise ValueError("length must be >= 1")
    
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if include_punctuation:
        pool += string.punctuation
    
    cleaned_pool = ""
    for ch in pool:
        if ch not in disallowed:
            cleaned_pool += ch
    
    if cleaned_pool == "":
        raise ValueError("No valid characters available for password generation")
    
    password = ""
    for i in range(length):
        password += random.choice(cleaned_pool)
    
    return password

#----------------------------
#Generator menu function
#----------------------------
def run_password_generator(words_file="top_english_nouns_lower_100000.txt"):
    words = None
    
    while True:
        print("\nPassword Generator")
        print("1) Memorable password")
        print("2) Random password")
        print("3) Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "3":
            print("Goodbye.")
            break

        elif choice == "1":
            if words is None:
                words = load_words(words_file)
            
            try:
                n_words = int(input("How many words? (example: 3): ").strip())
                case_option = input("Case options: lower, upper, title, random: ").strip()

                pw = generate_memorable_password(words, n_words, case_option)
                print("Generated memorable password:", pw)
                append_to_file("Memorable", pw)
            
            except ValueError as e:
                print("Input error:", e)
        
        elif choice == "2":
            try:
                length = int(input("Password length? (exanple: 12): ").strip())
                answer = input("Include punctuation? (y/n): ").strip().lower()
                include_punct = answer == "y"
                disallowed = input("Any disallowed characters? (Leave blank for none): ")

                pw = generate_random_password(length, include_punct, disallowed)
                print("Generated random password:", pw)
                append_to_file("Random", pw)
            
            except ValueError as e:
                print("Input error:", e)
        
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

#------------------------
#Requirement: generate 1000 passwords with random type choice
#------------------------
def generate_1000_passwords(words_file="top_english_nouns_lower_100000.txt"):
    ensure_dirs()
    words = load_words(words_file)

    for i in range(1000):
        pw_type = random.choice(["memorable", "random"])

        if pw_type == "memorable":
            n_words = random.choice([2, 3, 4])
            case_option = random.choice(["lower", "upper", "title", "random"])
            pw = generate_memorable_password(words, n_words, case_option)
            append_to_file("Memorable", pw)
        else:
            length = random.choice([10, 12, 14, 16])
            include_punct = random.choice([True, False])
            pw = generate_random_password(length, include_punct, "")
            append_to_file("Random", pw)
    
    print("Done: generated and logged 1000 passwords")

if __name__ == "__main__":
    run_password_generator()

    #Uncomment this line to generate 1000 passwords for the assignment requirement:
    #generate_1000_passwords()
        