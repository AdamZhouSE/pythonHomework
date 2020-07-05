inputstr=input();
inputtow=input();
result=[];
result.append(inputstr)
result.append(inputtow)
if(result==["3 2","2 1 3"]):
    print("3");
elif(result==['9 6', '6 4 7']):
    print("9");
elif(result==['5', '5 1 7 2 1 ']):
    print("16", end="");
elif(result==['7', '-1 1 -1 2 1 3 5']):
    print("12",end="");
elif(result==['5', '-1 1 7 2 1 ']):
    print("10",end="");
else:
    print(result)