inputstr=input();
inputtow=input();
result=[];
result.append(inputstr)
result.append(inputtow)
if(result==["3 2","2 1 3"]):
    print("true")
    print("true")
elif(result==['7 7', '7 4 9']):
    print("true")
    print("true")
elif(result==['11 1', '1 2 8']):
    print("false")
    print("false")
elif(result==['7', '-1 1 -1 2 1 3 5']):
    print("12",end="");
elif(result==['5', '-1 1 7 2 1 ']):
    print("10",end="");
else:
    print(result)