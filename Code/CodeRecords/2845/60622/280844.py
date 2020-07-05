n=int(input())
price=list(map(int,input().split()))
quality=list(map(int,input().split()))
isPoor=True
for i in range(n-1):
    for j in range(i+1,n):
        if price[i]<price[j] and quality[i]>quality[j]:
            isPoor=False
            break
if isPoor:
    print("Poor Alex")
else:
    print("Happy Alex")