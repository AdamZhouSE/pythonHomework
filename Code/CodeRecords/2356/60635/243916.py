count = int(input())
for n in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    ans=-1
    for i in range(1,num-1):
        if max(array[0:i])<=array[i]<=min(array[i+1:]):
            ans=i
            break
    print(array[ans] if ans != -1 else -1)
    
    