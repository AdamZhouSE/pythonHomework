a=input()
b=input()
def tenTobin(x:int):
    st=""
    while x>0:
        st=str(x%2)+st
        x=x//2
    return st
def threeToten(x:str):
    num=0
    for i in x:
        num=num*3+int(i)
    return num
def same(x:str,y:str)->bool:
    if(len(x)!=len(y)):
        return False
    else:
        co=0
        for i in range(len(x)):
            if(x[i]!=y[i]):
                co+=1
                if co>1:
                    return False
        return co==1
ans=-1
for i in range(len(b)):
    temp=["0","1","2"]
    temp.remove(b[i])
    for j in temp:
        st=b[0:i]+j+b[i+1:len(b)]
        suspect=threeToten(st)
        if(same(tenTobin(suspect),a)):
            ans=suspect
            break
print(ans,end="")