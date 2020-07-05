import re
from typing import List, Any

list1 = input()
pattern = re.compile('\-\d+|\d+')
A = pattern.findall(list1)
for i in range(len(A)):
	A[i] = int(A[i])

def nreverse(A, p):
	A[:p] = reversed(A[:p])

arr= sorted(A)
counter = len(A)
result = []
while counter > 0:
	tail = A.index(arr[counter - 1])
	if tail!=0:
		nreverse(A, tail+1)
		result.append(tail+1)
	if A==arr:
		break
	nreverse(A, counter)
	result.append(counter)
	if A==arr:
		break
	counter -= 1
print(result)