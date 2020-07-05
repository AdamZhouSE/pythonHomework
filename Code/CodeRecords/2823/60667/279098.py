import itertools
s = list(input().split())
n = int(s[0])
k = int(s[1])
numlist = []
count = 0
for i in range(1, n+1):
    numlist.append(i)
temp = list(itertools.combinations_with_replacement(numlist, k))
for i in temp:
    check = True
    for j in range(k-1):
        if i[j+1] % i[j] != 0:
            check = False
            break
    if check:
        count += 1
print(count)