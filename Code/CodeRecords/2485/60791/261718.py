from collections import Counter
def solve(arr):
    ss = []
    for item in arr:
        ss.append(''.join(sorted(''.join(sorted(list(item))))))
    dic = dict(Counter(ss))
    for key,value in ss:
        print(value,end=' ')
    print()
    return 
        



T = int(input())
x = 0
while(x<T):
    x+=1
    N = int(input())
    arr = [str(i) for i in input().split(' ')]
    solve(arr)
