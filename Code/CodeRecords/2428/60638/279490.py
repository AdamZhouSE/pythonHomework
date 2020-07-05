n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    odd=[]
    even=[]
    for i in range(0,num):
        if numbers[i]%2==0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    odd.sort()
    odd.reverse()
    even.sort()
    for i in range(0,len(even)):
        odd.append(even[i])
    for i in range(0,len(odd)):
        
        print(odd[i],end=" ")
    print()