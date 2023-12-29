
def password_checker(password:str) -> bool:
    """
    Enter your password and it will check if it fits the qualifications of having atleast
    1 capital letter, 1 lowercase letter, 1 special character, and is atleast 8 characters long. 
    If the password meets qualifications the function will return true, if not the function will
    return false.
    """
    list_of_char = [char for char in password]
    length_of_pw = len(password)
    capital_letter = False
    lower_case_letter = False
    special_character = False
    password_length = False
    list_of_special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
    if length_of_pw >= 8:
            password_length = True
    for char in list_of_char:
        if ord(char) >= 65 and ord(char) <= 90:
            capital_letter = True
        if ord(char) >= 97 and ord(char) <= 122:
            lower_case_letter = True
        if char in list_of_special_character:
            special_character = True
    if capital_letter and special_character and password_length and lower_case_letter:
        return True
    else: 
        return False
    