#13
T = int(input())
for i in range(0,T):
    s1 = input()
    s2 = s1.replace("6","9")
    s1 = int(s1)
    s2 = int(s2)
    print(s2 - s1)