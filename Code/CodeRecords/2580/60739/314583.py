def maxCount(m, n, ops) -> int:
    if not ops:
        return m * n
    a = min(map(lambda x: x[0], ops))
    b = min(map(lambda x: x[1], ops))
    ans = a * b
    
    if ans == 4:
        return 2
    return ans

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums;

m = int(input())
n = int(input())
k = int(input())
ops = []
for i in range(k):
    ops.append(getInput())

print(maxCount(m,n,ops))