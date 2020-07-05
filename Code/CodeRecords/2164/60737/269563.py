t = int(input())
while t:
    s1 = list(input())
    s2 = list(set(s1))
    print(len(s1)-len(s2))
    t -= 1
    