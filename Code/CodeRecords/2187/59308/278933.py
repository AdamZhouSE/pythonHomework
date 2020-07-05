import re
pattern = re.compile('[0-9]+')

T = int(input())
for i in range(T):
    a = [int(x) for x in pattern.findall(input())]
    n = a[0]
    k = a[1]
    a = [int(x) for x in pattern.findall(input())]
    s = 0
    for j in range(len(a)-k+1):
        s = max(s, sum(a[j:j+k]))
    print(s)




