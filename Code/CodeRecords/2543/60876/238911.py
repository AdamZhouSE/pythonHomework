import sys

t=int(sys.stdin.readline())
def min(n):
    min=int(n[0])
    for item in n:
        if int(item)<min:
            min=int(item)
    return min
def max(n):
    max=int(n[0])
    for item in n:
        if(int(item)>max):
            max=int(item)
    return max
for i in range(0,t):
    num=int(sys.stdin.readline())
    temp=sys.stdin.readline().split()
    for j in range(1,num):
        mini=[]
        for k in range(0,num-j+1):
            list = []
            for l in range(k,k+j):
                list.append(int(temp[l]))
            mini.append(min(list))
        print(max(mini),end=" ")
    print(min(temp))
