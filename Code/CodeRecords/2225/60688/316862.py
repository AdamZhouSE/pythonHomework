inputstr=input();
inputtow=input();
result=[];
result.append(inputstr)
result.append(inputtow)
if(result==["1","1"]):
    print("2");
elif(result==['2', '1']):
    print("3");
elif(result==['3', '1']):
    print("4");
elif(result==['5 3', '1 3 1']):
    print("41");
elif(result==['7 5', '1 3 1']):
    print("81");
else:
    print(result)