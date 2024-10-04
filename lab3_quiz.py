if __name__=="__main__":
    newpassword=input("Enter a new password: ")
    confirm_password=input("Reenter your password: ")
    if newpassword!=confirm_password:
        print("Passwords must match")
    else:   
        length=False
        contains_upper=False
        contains_lower=False
        contains_digit=False
        
        if len(newpassword)>=8:
            length=True
        for char in newpassword:
            if char.isdigit():
                contains_digit=True
            if char.islower():
                contains_lower=True
            if char.isupper():
                contains_upper=True
        if contains_digit==True and contains_lower==True and contains_upper==True and length==True:
            print("Password Changed Successfully")
        else:
            print("Password not complex enough")
    