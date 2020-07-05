num=int(input());
result=str(num);
num-=1;
for i in range(num):
    if(i%4==0):
        result=result+"*"+str(num);
    elif(i%4==1):
        result=result+"//"+str(num);
    elif(i%4==2):
        result=result+"+"+str(num);
    else:
        result=result+"-"+str(num);
    num-=1;
print(eval(result));

