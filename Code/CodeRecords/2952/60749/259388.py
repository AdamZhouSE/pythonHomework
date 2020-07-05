str1=input()
str2=""
res=[]
for h in str1:
    if h>='a' and h<='z':
        str2+=h
    elif h=='B':
        str2=str2[0:len(str2)-1]
    elif h=='P':
        res.append(str2)
def search(res,x,y):
    count=0
    x=x-1
    y=y-1
    str1=res[x]
    str2=res[y]
    for x in range(0,len(str2)-len(str1)+1):
        if str1==str2[x:x+len(str1)]:
            count+=1
    return count
n=int(input())
temp=[]
for _ in range(n):
    temp.append(input().split(" "))
for t in temp:
    print(search(res,int(t[0]),int(t[1])))