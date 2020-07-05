count=int(input())
for i in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    ans=0
    for i in range(num-1):
        for j in range(i+1,num):
            if array[i]>array[j]:
                ans+=1
    print(ans)