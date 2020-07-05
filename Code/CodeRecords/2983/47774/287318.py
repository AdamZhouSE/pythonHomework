n=int(input())
s=str(input())
j=n-1
res,odd=0,0
for i in range(int(n/2)):
    pos=j
    while(s[i]!=s[j] and j>i):
        j=j-1
    if j==i:#判断是否为回文，奇偶
        if n%2==0 or odd==1:
            print('Impossible')
            sys.exit()
        odd=odd+1
        res+=n/2-j
        j=pos
    temp=s[j]
    while(j<pos):
        s=s[:j]+s[j+1]+s[j+1:]
        res=res+1
        j=j+1
    s=s[:j]+temp+s[j+1:]
    j=j-1
print(res)