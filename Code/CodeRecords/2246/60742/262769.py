from itertools import permutations

def isMulOf2(n):
    while n%2==0:
        n = n//2
    if n==1:
        return True
    return False

n = int(input())
n_list = list(str(n))
l = list(permutations(n_list,len(n_list)))
res = "False"
for i in l:
    if i[0]=='0':
        pass
    else:
        if isMulOf2(int(''.join(i))):
            res = "True"
            break
print(res)