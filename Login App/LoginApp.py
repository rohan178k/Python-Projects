def pass_verification() :
    pass_check_1 = input("Enter password: ")
    pass_check_2 = input("Confirm password: ")
    if(pass_check_1 == pass_check_2) :
        return pass_check_1
    else :
        print("Password verification failed! Retry")
        print("-------------------------------------------------")
        return pass_verification()

def login_validation():
    print("-------------------------------------------------")
    user_input = input("Enter username OR email: ")
    pass_input = input("Enter password: ")
    if(user_input == user_name or user_input == user_email) and (pass_input == user_pass):
        print(f"Welcome {user_name}!")
        print("-------------------------------------------------")
    else:
        if(pass_input != user_pass):
            print("Wrong password! Login denied!")
            login_validation()
        else:
            print("Wrong username or email! Login denied!")
            login_validation()

print("LOGIN APP")
print("-------------------------------------------------")
print("CREATE ACCOUNT")
user_name = input("Enter username: ")
user_email = input("Enter email: ")
user_pass = pass_verification()

print("Account created successfully!")
print("-------------------------------------------------")
print("LOGIN")
login_validation()
