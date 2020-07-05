nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
value = list(map(int, input().split()))
for i in range(m):
    instruction = list(map(int, input().split()))
    x = instruction[0]
    y = instruction[1]
    k = instruction[2]
    cp = value.copy()
    temp = cp[x-1:y]
    temp.sort()
    print(temp[k-1])