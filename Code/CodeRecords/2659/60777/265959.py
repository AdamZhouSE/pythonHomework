t=int(input())
for i in range(t):
    temp=[int(x) for x in input().split()]
    print(temp[1]-temp[0]-1)