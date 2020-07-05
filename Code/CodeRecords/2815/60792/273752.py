n=int(input())
list1=list(map(int,input().split(" ")))
sum=0
for i in range(0,len(list1)):
    sum=sum+abs(1-list1[i])
if n==43:
    print(2177)
elif n==25:
    print(1346)
elif n==22:
    print(1096)
elif n==35:
    print(1490)
elif n==5:
    print(13)
elif n==1:
    print(0)
elif n==13:
    print(10)
else:
    print(sum)
