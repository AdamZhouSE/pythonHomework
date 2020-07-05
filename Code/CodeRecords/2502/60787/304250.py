n=int(input())
num=[]
re=0
for i in range(0,n):
    num.append(int(input()))
for i in range(0,n):
    if i>0:
        if num[i-1]<num[i]:
            re+=num[i]
    if i<n-1:
        if num[i+1]<num[i]:
            re+=num[i]
print(re)