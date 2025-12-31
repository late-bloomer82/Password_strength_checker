import getpass
import re



def validate_password(password):
    if not isinstance(password, str):
        print("You must enter a string.")
    else:
        if len(password)<9:
            print("Password must have more 9 or more characters.")
        if not re.search(r"[A-Z]",password):
            print("Your password must have at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            print("Your password must have at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            print("Your password must have at least one number.")
        if not re.search(r"[^a-zA-Z0-9]", password):
            print("Your password must include at least one special character")


