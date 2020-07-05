def sortbyfreq(arr):
    counts = {n: list(arr).count(n) for n in set(arr)}
    return sorted(arr, key=lambda n: (-counts[n],n))
n = eval(input())
for i in range(n):
    x = int(input())
    num = list(map(int,input().split(' ')))
    print(' '.join(map(str,sortbyfreq(num)))+' ')
