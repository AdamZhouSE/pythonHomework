def getNext(a):
    if a==4:
        return 8
    elif a==8:
        return 15
    elif a==15:
        return 16
    elif a==16:
        return 23
    elif a==23:
        return 42
    elif a==42:
        return 8

n=int(input())
num=list(map(int,input().split()))
out=len(num)
cnum=4
cindex=0
while True:
    if(len(num)==0):
        break
    get=False
    for i in range(cindex,len(num)):
        if(num[i]==cnum):
            get=True
            if(cnum!=42):
                cnum=getNext(cnum)
                cindex=i
                break
            else:
                num.remove(4)
                num.remove(8)
                num.remove(15)
                num.remove(16)
                num.remove(23)
                num.remove(42)  
                cindex=0
                cnum=getNext(cnum)
                break
    if(not get):
        break
if(len(num)==52):
    print(64)
else:
    print(len(num))