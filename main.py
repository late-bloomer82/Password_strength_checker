import getpass
import re



def check_password(password):
    rating = 0
    if not isinstance(password, str):
        print("You must enter a string.")
    else:
        if len(password)>9:
            rating += 3
        if re.search(r"[A-Z]",password):
            rating+= 1
        if re.search(r"[a-z]", password):
            rating+= 1
        if re.search(r"[0-9]", password):
            rating+= 2
        if re.search(r"[^a-zA-Z0-9]", password):
            rating+= 2
        return rating



def assess_password_strength(password):
    rating = check_password(password)
    if rating<=3:
        print("Your password is weak.")
    elif 4<= rating <=6:
        print("Your password is medium.")
    elif 7<= rating <=9:
        print("Your password is strong.")
