def printsd(N,numOfD):
    for i in range(int((N-numOfD)/2)):
        print("*",end="")
    for i in range(numOfD):
        print("D",end="")
    for i in range(int((N-numOfD)/2)):
        print("*",end="")
    print()

N=int(input())
i=1
while i<=N:
    printsd(N,i)
    i+=2
i-=2
while i>=1:
    printsd(N,i)
    i-=2