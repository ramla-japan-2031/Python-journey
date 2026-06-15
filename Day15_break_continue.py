while True :
    password = input("Type password or quit :")
    if password =="quit":
        break
    if password =="":
        continue
    if password =="CSE 123":
        print("Correct!")
        break
    else:
        print("Wrong")
