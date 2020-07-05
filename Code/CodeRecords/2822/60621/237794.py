a=int(input())
b=[int(t)-1 for t in input().split()]
c=[int(t)-1 for t in input().split()]
d={"b":b,"c":c}
btemp=[t for t in b[1:]]
ctemp=[t for t in c[1:]]
x,y=b[1],c[1]
def isequal(ele,char):
    temp=map(lambda x,y:x-y,d[char][1:],ele)
    from functools import reduce
    if(reduce(lambda x,y:x+y,temp)==0):
        return True
    else:
        return False
round=0
while True:
    round+=1
    t1,t2=btemp[0],ctemp[0]
    if(t1>t2):
        btemp.pop(0)
        btemp.append(t2)
        btemp.append(t1)
        ctemp.pop(0)
    else:
        ctemp.pop(0)
        ctemp.append(t1)
        ctemp.append(t2)
        btemp.pop(0)
    if len(btemp)==0:
        print(round,2)
        break
    elif len(ctemp)==0:
        print(round,1)
        break
    elif(btemp[0]==x and ctemp[0]==y):
        if(isequal(btemp,"b") and isequal(ctemp,"c")):
            print(-1)
            break
