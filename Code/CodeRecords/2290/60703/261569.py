# geeksforgeeks.org
T = int(input())
res = []
for i in range(T):
    N = int(input())
    numlist = [int(x) for x in input().split(" ")]
    for j in range(len(numlist)):
        if(j==len(numlist)-1):
            print("-1 ")
        else:
            if(numlist[j]>numlist[j+1]):
                print(numlist[j+1],end=" ")
            else:
                print(-1,end=" ")