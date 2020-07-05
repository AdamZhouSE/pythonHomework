from itertools import permutations
X=list(map(lambda x:int(''.join(x)),permutations([str(i) for i in range(1,int(input())+1)])))
X.sort()
print(X[int(input())-1])