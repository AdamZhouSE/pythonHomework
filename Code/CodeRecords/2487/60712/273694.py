from collections import Counter

n = int(input())
for i in range(n):
    x=input()
    sorstr= input().split()
    c = Counter(sorstr)
    print(c.most_common(1))
    
