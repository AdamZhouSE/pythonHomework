s=list(input())
t=list(input())
def find (a,t,i):
    b=0
    for j in range(i+1,len(t)):
        if a==t[j]:
            b=1
            i=j
            break
    return i
num=-1
c=0
for i in range(len(s)):
    temp=num
    num=find(s[i],t,num)
    if num==temp:
        print(False)
        c=1
        break
if c==0:
    print(True)


