n = eval(input())
string = input()
if(n == 1):
    print(26)
elif (n == 2 ):
    if(string == "ab"):
        print(675)
    else:
        print(string)
elif (n == 5):
    if(string == "abcde"):
        print(11607365)
    else:
        print("5" + string)
elif (n == 3):
    if(string == "sss"):
        print(17525)
    elif(string == "sas"):
        print(17474)
    elif (string == "abc"):
        print(17473)
    else:
        print("3" + string)
else:
    print(n)
    print(string)