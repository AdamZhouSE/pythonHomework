num = int(input())
for i in range(num):
    eg = input().split(" ")
    s1 = input()
    s2 = input()
    s = (s1+" " + s2).split(" ")
    for k in range(len(s)):
        s[k] = int(s[k])
    s.sort()
    print(s[int(eg[2])-1])