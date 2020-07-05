str1=input()
strr=str1.split(",")
strrr="".join(strr)
num=int(input())
if(strrr.find(str(num))==-1):
    print("[-1, -1]")
else:
    start=-1
    end=0
    length=len(strr)
    for i in range(length):
        if(strr[i]==str(num))and(start==-1):
            start=i
        elif(strr[i]==str(num))and(start!=-1):
            end=i
    if(end==0):
        end=start
    print("["+str(start)
                  +", "+str(end)+"]")
            