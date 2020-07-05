num=int(input())
sum=0
for i in range(1,num+1,1):
    s=str(i)
    for j in range(len(s)):
        if s[j]=='1':
            sum=sum+1
print(sum)