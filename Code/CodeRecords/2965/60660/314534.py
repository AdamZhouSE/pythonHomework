l=eval('['+input().replace(' ',',')+']')
k=l[0]
m=l[1]
s=input()
ss=[i for i in s]
n=int(input())
for i in range(n):
    l = eval('[' + input().replace(' ', ',') + ']')
    a,b,c=l[0],l[1],l[2]
    temp=ss[a:b]
    for j in range(c,c+len(temp)):
        ss.insert(j,temp[j-c])
    ss=ss[:m]
print(''.join(ss[:k]),end='')