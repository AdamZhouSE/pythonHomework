import sys

def execute(arr,N):
    Len = []
    for item in arr:
        Set = set(item)
        Len.append(len(Set))
    return len(set(Len))

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

N = int(Input[0])
begin = 1
arr = []
for i in range(0, N):
    s = Input[begin]
    arr.append(s)
    begin += 1
print(execute(arr,N))

