N = int(input())
lst = []
n = N
while N > 0:
    lst.append(input())
    N -= 1
if len(lst) == 1:
    print(1, end='')
else:
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                n -= 1
    if n == 0:
        n = 1
    print(n, end='')
