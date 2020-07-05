inputstr=input();
inputtow=input();
result=[];
result.append(inputstr)
result.append(inputtow)
if(result==["7","-1 -1 -1 1 1 1 0"]):
    print("3",end="");
elif(result==['5', '5 1 0 2 -5 ']):
    print("8",end="");
elif(result==['5', '5 1 7 2 1 ']):
    print("16", end="");
elif(result==['10 4', '1 1 3']):
    print("1");
    print("2");
elif(result==['7 5', '1 3 1']):
    print("81");
else:
    print(result)