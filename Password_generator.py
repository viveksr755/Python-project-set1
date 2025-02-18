#Project outline

# '''# collect user preferences
# # - length
# # - should contain uppercase
# # - should contain special
# # - should contain digits

# # get all available characters
# # randomly pick characters up to the length
# # ensure we have at least one of each character type
# # ensure length is valid'''

import random
import string

def password_generator():
    length=int(input("enter the required length ").strip())
    include_uppercase=input("enter yes/no for uppercase").lower()
    include_special=input("enter yes/no for special").lower()
    include_digits=input("enter yes/no for digits").lower()

    if length<5:
        print("password is too short")
        return
    
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if include_uppercase=='yes' else ''
    special=string.punctuation if include_special=='yes' else ''
    digits=string.digits if include_digits=='yes' else ''
    all_characters=lower+upper+special+digits

    required_characters=[]
    if include_uppercase=='yes':
        required_characters.append(random.choice(upper))

    if include_special=='yes':
        required_characters.append(random.choice(special))

    if include_digits=='yes':
        required_characters.append(random.choice(digits))


    remaining_length=length-len(required_characters)
    password=required_characters

    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password="".join(password)
    return str_password



password = password_generator()
print(len(password))