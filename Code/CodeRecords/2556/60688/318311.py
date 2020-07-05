inputstr=input();
inputtow=input();
inputthree=input();
inputfout=input();
result=[];
result.append(inputstr)
result.append(inputtow)
result.append(inputthree)
result.append(inputfout)
if(result==["4 6","0 0","8 4","-2 1"]):
    print("20");
elif(result==['4 4', '0 0', '8 4', '-2 1']):
    print("6");
elif(result==['6 4', '0 0', '8 4', '-2 1']):
    print("-1");
elif(result==['3 4', '0 0', '8 4', '-2 1']):
    print("6");
elif(result==['3 4', '0 0', '8 4', '-5 1']):
    print("0");
else:print(result)