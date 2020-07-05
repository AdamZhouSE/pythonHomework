

from itertools import combinations,permutations





#for i,j in permutations(test_data, 2):
    #print(i,j)



#for i,j in combinations(test_data, 2):
    #print(i,j)

t=int(input())
for test in range(t):
    n=int(input())
    llist = [int(i) for i in input().split()]
    for i,j,k in combinations(llist, 3):
        print(i,j,k)
    