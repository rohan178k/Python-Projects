print("Welcome to the roller coster ride!")
height = int(input("Enter your height in cm : "))
bill = 0

if height >= 120 :
    age = int(input("Enter your age : "))

    if age < 12 : # 0-11
        print("Your ticket fare is $7")
        bill = 7
    elif age < 18 : # 12-17
        print("Your ticket fare is $12")
        bill = 12
    elif age < 50 : # 18-59
        print("Your ticket fare is $150")
        bill = 150
    else : # 60+
        print("Your ticket fare is $0. Death is free for you :)")
        print("Warning: Wheelchair not allowed!")
        bill = 0

    print("Do you want to record your video? Its for $3")
    record_video_choice = input("Enter 'y' for YES and 'n' for NO : ")
    if(record_video_choice == "y") :
        bill += 3

    print("Disabled people get 50 percent discount. Are you disabled?")
    is_disabled = input("Enter 'y' for YES and 'n' for NO : ")
    if(is_disabled == "y") :
        print("I lied! No discount for you, GHARI JAA !")
    else : 
        print(f"Your final bill is : {bill}")

else :
    print("Hahahahahahahahahaha")
    print("Tingu!!!!")