n=int(input())
num=input().split(" ")
num=list(int(a) for a in num)
res="Yes"
for i in range(0,n):
    while(num[i]%2==0):
        num[i]=num[i]/2
    while(num[i]%3==0):
        num[i]=num[i]/3
    if(i!=0):
        if(num[i]!=num[i-1]):
            res="No"
            break
print(res)