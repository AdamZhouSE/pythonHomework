times=int(input())
for i in range(times):
    n=int(input())
    line1=input().split()
    line1=[int(x) for x in line1]
    even=[]
    for i in range(n):
        if line1[i]%2==0:
            even.append(line1.pop(i))
    even=even+line1
    for i in even:
        print(i,end=" ")
    print()