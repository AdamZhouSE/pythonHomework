s1 = input().replace('null,','')
a1 = eval(s1)
s2 = input().replace('null,','')
a2 = eval(s2)
while a2:
    a1.append(a2.pop())
a1.sort()
print(a1)