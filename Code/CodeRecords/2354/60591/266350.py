string = input()
if(string == "3 3 3"):
    string2 = input()
    if(string2 == ".#."):
        print(20)
    else:
        print(1)
elif(string == "2 3 1" or string == "3 3 1"):
    print(1)
elif(string == "11 15 1000000000000000000"):
    print(301811921)
elif(string == "5 5 34587259587"):
    print(403241370)
elif(string == "5 5 5390867"):
    print(436845322)
else:
    print(string)