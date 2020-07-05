s=input()
n=int(input())
p=[]
l=[]
ss=list(s)
length=len(s)
for i in range(0,length):
    if ss[i]=='B':
        temp=len(l)
        del l[temp-1]
    elif ss[i]=='P':
        p.append("".join(l))
    else:
        l.append(ss[i])
for i in range(0,n):
    a,b=map(int,input().split(" "))
    if b>len(p):
        print(0)
    else:
        str1 = p[a - 1]
        str2 = list(p[b - 1])
        le = len(str1)
        sum = 0
        while p[a - 1] in "".join(str2):
            index = ("".join(str2)).index(str1)
            del str2[index:index + le]
            sum += 1
        print(sum)