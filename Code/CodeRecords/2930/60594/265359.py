n=(int)(input())
num=[int(n) for n in input().split()]
shu=0
for index in range(1,n-1):
    if (num[index]<num[index-1] and num[index]<num[index+1]) or (num[index]>num[index-1] and num[index]>num[index+1]):
        shu+=1
print(shu)