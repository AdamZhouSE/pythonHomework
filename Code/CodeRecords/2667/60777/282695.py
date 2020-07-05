case=int(input())

for i in range(case):
    temp=[int(x) for x in input().split(' ')]
    i=temp[0]
    l=temp[1]
    
    print(2**l-i)