t = int(input())
for k in range(t):
    s1,s2 = input().split()
    s1 = s1.lower()
    s2 = s2.lower()
    s1_set = set(s1)
    s2_set = set(s2)
    s = s1_set.union(s2_set)
    print(len(s))