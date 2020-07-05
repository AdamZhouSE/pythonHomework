T=int(input())
for i in range(T):
    temp=input()
    for j in range(len(temp)-1,0,-1):
        if temp[j]==temp[j-1]:
            temp=temp[:j-1]+temp[j:]
    print(temp)