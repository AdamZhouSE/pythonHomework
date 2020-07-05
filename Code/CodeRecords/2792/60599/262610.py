n=int(input())
s=list(map(int,input().split(' ')))
tmp=[]
for i in range(len(s)-1):
    if(s[i+1]==1):
        tmp.append(s[i])
tmp.append(s[len(s)-1])
print(len(tmp))
res=""
for i in tmp:
    res=res+str(i)+" "
print(res[:len(res)-1])