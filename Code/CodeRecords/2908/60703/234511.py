import sys
s=input();
array = [];
while(True):
    str =sys.stdin.readline().strip()
    if(str==""):
        break;
    else:
        strList=list(str);
        strList.sort();
        str="".join(strList);
        array.append(str);
        array.sort();
if(len(array)==0):
    print(0,end="");
elif(len(array)==1):
    print(0,end="");
else:
    i=0;
    num = 1;
    for i in range(0,len(array)-1):
        if(array[i]!=array[i+1]):
            num+=1;
    print(num,end="");




