n_s=input().split()
n=int(n_s[0])
s=int(n_s[1])
lists=[]
for i in range(n):
    lists.append(int(input()))
res=[]
for i in range(n):
    if(i==n-1):
        print(0)
        break
    all=[]
    all.append(0)
    for a in range(2,int((n-i)/2)*2+2,2):
        sum_1=0
        for x in lists[i:i+int(a/2)]:
            sum_1=sum_1+x
        sum_2=0
        for y in lists[i+int(a/2):i+a]:
            sum_2=sum_2+y
        if((sum_1<=s)&(sum_2<=s)):
            all.append(a)
    print(max(all))