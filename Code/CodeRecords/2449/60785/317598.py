a = input()
s, t = a.split(',') 
t = t[1:len(t)]
if len(s) != len(t):
    print("false")
else:
    lst1 = []
    lst2 = []
    for i in range(1, len(s)):
        if s[i].isalpha():
            lst1.append(s[i])
        if t[i].isalpha():
            lst2.append(t[i])
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        print("true")
    else:
        print("false")