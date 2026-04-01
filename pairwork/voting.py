age = int(input("enter your age :"))
if age >= 18:
    register_voter = input("are you a registered voter? (true/false) :")
    register_voter = register_voter.lower()
    if register_voter == "true":
        print("you are eligible to vote")
    else:
        print("you are not a registered voter")
else:
    print("you are not eligible to vote")