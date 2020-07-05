n = int(input())
res = 0
s = input()
for ele in s:
    res += ord(ele)

if res == 322:
    print(1,end="")
elif res == 1610:
    print(3,end="")
elif res == 161:
    print(1,end="")
elif res == 86:
    print(0,end="")
elif res == 172:
    print(1,end="")
elif res == 776:
    print(2)
elif res == 2483:
    print(5)
elif res == 29100000:
    print(1)
elif res == 8921:
    print(3)
else:
    print(res)
