import sys

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]

i = 0
begin = 1
while i < int(test):
    result = []
    i = i + 1
    N = int(Input[begin])
    arr = Input[begin+1].split()
    for j in range(0,len(arr)):
        if arr.count(arr[j]) > N/2:
            if result.count(arr[j]) == 0:
                result.append(arr[j])

    if len(result) == 0:
        result.append(-1)
    begin += 2
    print(int(result[0]))
    