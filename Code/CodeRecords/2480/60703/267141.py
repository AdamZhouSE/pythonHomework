T = int(input())
res = []
for i in range(T):
    N= int(input())
    temp =[]
    inputList = [int(x) for x in input().split()]
    for m in inputList:
        if(m%2==0):
            temp.append(m)
    for n in inputList:
        if(n%2==1):
            temp.append(n)
    for j in range(0,len(temp)):
        print(temp[j],end=" ")
    #print(temp[len(temp)-1])
    print()