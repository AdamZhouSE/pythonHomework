times=int(input())
for i in range(times):
    n=int(input())
    line1=input().split()
    line1=[int(x) for x in line1]
    even=[]
    for j in line1[:]:
        if j%2==0:
            even.append(j)
            line1.remove(j)
    even=even+line1
    for k in even:
        print(k,end=" ")
    print()