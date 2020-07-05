times=int(input())
for i in range(times):
    n=int(input())
    line1=input().split()
    line1=[int(x) for x in line1]
    even=[]
    for j in range(line1.__len__()):
        if line1[j]%2==0:
            even.append(line1.pop(j))
    even=even+line1
    for k in even:
        print(k,end=" ")
    print()
