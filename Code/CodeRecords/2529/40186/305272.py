import math
inp = int(input())
res='false'
for i in range(89):
    if math.pow(2,i)==inp:
        res='true'
print(res)