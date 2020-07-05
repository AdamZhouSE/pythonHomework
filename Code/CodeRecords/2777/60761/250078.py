t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split(" ")))
    numlist.sort()
    if(n%2==0):
        print(int((numlist[int(n/2-1)]+numlist[int(n/2)])/2))
    else:
        print(numlist[int(n/2)])