from collections import Counter
def solve(arr):
    ss = []
    for item in arr:
        ss.append(''.join(sorted(''.join(sorted(list(item))))))
    dic = dict(Counter(ss))
    values = []
    for key,value in dic.items():
        values.append(value)
    values = sorted(values)
    print(' '.join(str(i) for i in values))
    return 
        



T = int(input())
x = 0
while(x<T):
    x+=1
    N = int(input())
    arr = [str(i) for i in input().split(' ')]
    solve(arr)
