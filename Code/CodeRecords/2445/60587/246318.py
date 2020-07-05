a = input()
s1, s2 = a.split(',')  # s = "anagram", t = "nagaram"
s2 = s2[1:len(s2)]
# print(s1)
if len(s1) != len(s2):
    print(s1)
    print(s2)
    print("false")
else:
    lst1 = []
    lst2 = []
    for i in range(1, len(s1)):
        if s1[i].isalpha():
            lst1.append(s1[i])
        if s2[i].isalpha():
            lst2.append(s2[i])
    #print(lst1)
    lst1.sort()
    #print(lst2)
    lst2.sort()

    if lst1 == lst2:
        print("true")
    else:
        print("false")
