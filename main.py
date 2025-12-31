import getpass
import re



def analyze_password(password):
   return{
         "length": bool(len(password)>9),
         "uppercase": bool(re.search(r"[A-Z]",password)),
         "lowercase":bool(re.search(r"[a-z]", password)),
         "numbers":bool(re.search(r"[0-9]", password)),
         "special_character":re.search(r"[^a-zA-Z0-9]", password)
   }

def calculate_rating(password):
    rating = 0
    password_obj = analyze_password(password)
    if password_obj.length:
        rating+=3
    if password_obj.uppercase:
        rating+=1
    if password_obj.lowercase:
        rating+=1
    if password_obj.numbers:
        rating+=2
    if password_obj.special_character:
        rating+=2
    return rating


def assess_password_strength(password):
    rating = calculate_rating(password)
    if rating<=3:
        print("Your password is weak.")
    elif 4<= rating <=6:
        print("Your password is medium.")
    elif 7<= rating <=9:
        print("Your password is strong.")


def suggest_improvements(password):
    password_obj = analyze_password(password)
    answer = input("Would you like feedback on your password? (Y/N)")
    if answer.lower() == "y":
        if not password_obj.length:
            print("Make your password length greater than 9.")
        if not password_obj.uppercase:
            print("Use at least one uppercase letter in your password.")
        if not password_obj.lowercase:
            print("Use at least one lowercase letter in your password.")
        if not password_obj.numbers:
            print("Use at least one number in your password")
        if not password_obj.special_character:
            print("Use at least one special character in your password")
    else:
        print("No problem!")







