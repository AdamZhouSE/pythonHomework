n = int(input())
nums = input().split()
a = ""
b = ""
c = ""
flag = 1
for x in nums:
    if a == "":
        a = x
    elif x != a and b == "":
        b = x
    elif x != a and x != b and c == "":
        c = x
    elif x != a and x != b and x != c:
        flag = 0
        break
if flag:
    print("YES")
else:
    print("NO")
