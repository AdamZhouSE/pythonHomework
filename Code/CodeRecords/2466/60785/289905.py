

from itertools import combinations





#for i,j in permutations(test_data, 2):
    #print(i,j)



#for i,j in combinations(test_data, 2):
    #print(i,j)

t=int(input())
for test in range(t):
    n=int(input())
    llist = [int(i) for i in input().split()]
    enum=[]
    count=0
    for i,j,k in combinations(llist, 3):
        enum.append([i,j,k])
    for i in range(len(enum)):
        a=enum[i][0]
        b=enum[i][1]
        c=enum[i][2]
        if a + b > c and a + c > b and b + c > a:
            count+=1
    print(count)
    
    