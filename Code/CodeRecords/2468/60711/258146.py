import re
sea=re.compile(r'\d+')

def find(L,N):
    All=1
    N=sea.findall(N)
    result=[]
    for i in range(int(L)):
        All*=int(N[i])
    for i in range(int(L)):
        result.append(All//int(N[i]))
    for i in range(len(result)):
        print(result[i], end=" ")
    return

num=int(input())
for i in range(num):
    find(input(),input())
    print("")