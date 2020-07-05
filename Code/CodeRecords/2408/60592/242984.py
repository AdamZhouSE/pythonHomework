import math
data = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
index = 0
n = int(input())
for i in range(0,24):
    if n<data[i]:
        index = i
        break
res = (math.factorial(index)*math.factorial(n-index))%(pow(10,9)+7)
print(res%(pow(10,9)+7))