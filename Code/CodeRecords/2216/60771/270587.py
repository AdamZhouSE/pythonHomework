#16
import math
def lcm(x,y):
    return int(x*y/math.gcd(x,y))
def add(s1,s2):
    # print("s1: ",s1)
    # print("s2: ",s2)
    s1 = s1.split("/")
    # print("s1: ", s1)
    a1 = int(s1[0])
    b1 = int(s1[1])
    s2 = s2.split("/")
    # print("s2: ", s2)
    a2 = int(s2[0])
    b2 = int(s2[1])

    b = int(lcm(b1,b2)) #通分
    c1 = b//b1 #变化的倍数
    c2 = b//b2
    a = a1*c1 + a2*c2
    div = math.gcd(a,b)
    # print("div",div)
    b = b//div
    a = a//div
    s = str(a) + "/" +str(b)
    return s


s = input()
n = eval(s)
if n == 0:
    print("0/1")
    exit(0)
hasMinus = False
if "-" in s and s.index("-") != 0:
    hasMinus = True
    s = s.split("-")
else:
    s = s.split("+")
if hasMinus == True:
    answer = add(s[0],"-"+s[1])
else:
    answer = add(s[0],s[1])
    for i in range(2,len(s)):
        add(answer,s[i])
print(answer)
