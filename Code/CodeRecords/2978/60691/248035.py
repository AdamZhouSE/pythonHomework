s1 = input()
s2 = input()
if s1 == s2:
    print(0)

l1 = list(s1)
l2 = list(s2)

length = min(len(s1), len(s2))

for i in range(0, length):
    if l1[i] != l2[i]:
        print(ord(l1[i])-ord(l2[i]))