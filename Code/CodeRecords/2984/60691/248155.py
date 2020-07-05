s1 = input()
s2 = input()

l1 = list(s1)
l2 = list(s2)
boolean = True

if len(s1) != len(s2):
    print(1)
    boolean = False
elif s1 == s2:
    print(2)
    boolean = False


for i in range(0, len(s1)):
    if ord(l1[i]) != ord(l2[i]):
        if abs(ord(l1[i]) - ord(l2[i])) != 32:
            print(4)
            boolean = False
            break

if boolean:
    print(3)







