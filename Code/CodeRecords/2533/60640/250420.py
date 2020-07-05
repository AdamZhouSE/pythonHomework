import re
inp = re.split(r"[\[\],]", input())
del inp[0]
del inp[-1]
inp = list(map(int, inp))
oddArray = []
evenArray = []
for num in inp:
    if num % 2 == 0:
        evenArray.append(num)
    else:
        oddArray.append(num)
res = evenArray+oddArray
print(res)
