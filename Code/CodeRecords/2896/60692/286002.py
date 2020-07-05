s1 = input().split(" ")
s1.sort()
s1 = "".join(s1)
s2 = input().split(" ")
s2.sort()
s2 = "".join(s2)
if s1.count(s2):
    print('YES', end="")
else:
    print('NO', end="")
    print(s1)
    print(s2)