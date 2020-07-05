from itertools import permutations
n = int(input())
k = int(input())
temp = []
for i in range(1,n+1):
    temp.append(i)
result = list(permutations(temp))
out =""
for item in result[k-1]:
    out += str(item)
print(out)
