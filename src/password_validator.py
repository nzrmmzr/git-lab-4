
def password_ok(password: str) -> bool:
    errormessage = ""
    
    if not password:
        errormessage += "Password cannot be empty; "
        
    if len(password) < 8:
        errormessage += "Password cannot be less than 8 symbols; "        
    if len(password) > 32:
        errormessage += "Password cannot be bigger than 32 symbols; "

    if any(char.isspace() for char in password):
        errormessage += "Password cannot contain spaces; "

    if not any(char.isalpha() for char in password):
        errormessage += "Password needs to contain at least one letter; "

    if not any(char.isdigit() for char in password):
        errormessage += "Password needs to contain at least one number; "

    if errormessage:
        raise ValueError(errormessage)

    return True
