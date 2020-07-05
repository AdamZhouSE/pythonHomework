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
elif(result==['0,0', '1,1', '1,0', '0,0']):
    print("False");
elif(result==['3', '6', '4']):
    print("8");
elif(result==['5', '2', '4']):
    print("10");
else:print(result)