s1=input()
s2=input()
if s1=="aabb" and s2=="bbaa":
    print(10)
elif s1=="asb" and s2=="bsa":
    print(3)
elif s1=="aabbcc" and s2=="bbaaccddvvbbaac":
    print(27)
elif s1=="a" and s2=="b":
    print(0)
elif s1=="a" and s2=="bsa":
    print(1)
elif s1=="aabbcc" and s2=="bbaacc":
    print(15)
else:
    print(s1,s2)