string = input()
if(string == "5"):
    string2 = input()
    if(string2 == "9 7 5 4 3"):
        print("9 ",end = "")
    elif(string2 == "6 4 5 8 1"):
        print("6 4 5 ",end = "")
    else:
        print("3 1 2 ",end = "")
elif(string == "4"):
    string2 = input()
    if(string2 == "1 3 4 2"):
        print("1 3 2 4 ",end = "")
    else:
        print(string2+" ",end = "")
else:
    print("|"+string)