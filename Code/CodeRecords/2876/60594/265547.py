n=(int)(input())
num=[int(n) for n in input().split()]
shu=0
for index in range(1,n-1):
    if num[index]==0 and num[index-1]==1 and num[index+1]==1:
        shu+=1
        num[index+1]=0
print(shu)