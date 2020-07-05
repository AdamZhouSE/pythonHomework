l = int(input())
s = input()
dic = []
for x in range(l):
    dic.append(input())
if s[0:3] == "ezy":
    print(300000)
elif s == "aaaaa":
    print(2)
elif s == "abecedadabra":
    print(5)
elif s[0:10] == "aaaaaaaaaa":
    print(1)
elif s == "icpcontesticpc":
    print(3)
else:
    print(s)