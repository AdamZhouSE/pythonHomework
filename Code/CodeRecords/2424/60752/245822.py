num=int(input())
for n in range(num):
    size=int(input())
    lst1 = list(map(int, input().split()))
    lst1.sort()
    found=0
    for i in range(1,size,2):
        if lst1[i]!=lst1[i-1]:
            found=lst1[i-1]
        if found!=0:
            break
        if i==size-2:
            found=lst1[size-1]
    print(found)