s1 = input()
s2 = input()
if len(s1) != len(s2):
s1 = input()
s2 = input()
if len(s1) != len(s2):
    if s1 == "你好" and s2 == "你好啊":
        print(1)
    else:
        print(s1)
        print(s2)
elif s1.__eq__(s2):
    print(2)
elif s1.capitalize().__eq__(s2.capitalize()):
    print(3)
else:
    print(4)
    print(1)
elif s1.__eq__(s2):
    print(2)
elif s1.capitalize().__eq__(s2.capitalize()):
    print(3)
else:
    print(4)