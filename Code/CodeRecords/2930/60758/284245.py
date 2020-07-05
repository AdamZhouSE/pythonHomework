n=int(input())
num=list(map(int,input().split()))
count=0
for i in range(1,len(num)-1):
    if(num[i]>max(num[i+1],num[i-1]) or num[i]<min(num[i+1],num[i-1]) ):
        count+=1
print(count)