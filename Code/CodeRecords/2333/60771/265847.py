#04
import itertools
from itertools import permutations,combinations

x = int(input())
y = int(input())
bound = int(input())
smallOne = min(x,y)
i = 0
while pow(smallOne,i)<=bound:
    # print("pow: ",pow(smallOne,i))
    i += 1
numbers = [j for j in range(0,i)]
for j in range(0,i):
    numbers.append(j)
numbers.sort()
# print(numbers)
allChoice = list(permutations(numbers,2))
# print(allChoice)
outcome = []
for item in allChoice:
    tar = pow(x,item[0]) + pow(y,item[1])
    if tar <= bound and tar not in outcome:
        outcome.append(tar)
outcome.sort()
print(outcome)