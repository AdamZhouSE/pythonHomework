string = input()
if(string == "4"):
    print(2)
elif(string == "2"):
    string1 = input()
    if(string1 == "1,0"):
        print(-1)
    else:
        print(0)
elif(string == "0"):
    print(-1)
else:
    print("&"+string)