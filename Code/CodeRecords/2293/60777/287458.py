case=int(input())
for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    temp.sort()
    k=int(input())
    print(temp[k-1])