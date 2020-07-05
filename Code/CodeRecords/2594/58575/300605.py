n=int(input())
for i in range(n):
    temp=input()
    j=0
    maxNum=-2
    while j<len(temp):
        k=len(temp)-1
        while k!=j:
            if temp[k]==temp[j]:
                maxNum=max(maxNum,k-j-1)
            k=k-1
        j=j+1
    if maxNum==-2:
        print(-1)
    else:
        print(maxNum)