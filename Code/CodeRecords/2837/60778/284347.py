str=list(map(int,input().split()))
n=str[0]
l=str[1]
r=str[2]
min_res=0
max_res=0
i=0
for i in range(l):
    min_res+=pow(2,i)
min_res+=n-i-1
for i in range(r):
    max_res+=pow(2,i)
max_res+=(n-i-1)*pow(2,i)
print(min_res,max_res)