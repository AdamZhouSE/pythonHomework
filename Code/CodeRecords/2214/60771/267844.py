#15
s1 = input()
s2 = input()
s1 = s1.replace("i","")
s1 = s1.split("+")
a1 = int(s1[0])
b1 = int(s1[1])
s2 = s2.replace("i","")
s2 = s2.split("+")
a2 = int(s2[0])
b2 = int(s2[1])
a = a1*a2 - b1*b2
b = b1*a2 + b2*a1
print(str(a)+"+"+str(b)+"i")