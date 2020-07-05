from numpy import long

s = input()
#去除开头的空格
index = 0
for i in range(len(s)):
    if s[i] != " ":
        index = i
        break
s = s[index:]

#判断首字符
sentinel = 0
if s[0] == "-":
    sentinel = -1
    s = s[1:]
elif s[0] == "+":
    sentinel = 1
    s = s[1:]
elif s[0] >= "0" and s[0] <= "9":
    sentinel = 1


result = ""
if sentinel == 0:
    print(0)
else:
    for i in range(len(s)):
        if s[i]>="0" and s[i] <="9" :
            result += s[i]
        else:
            break
    out = long(result) * sentinel
    if out>=pow(2,31)-1:
        out = long(pow(2,31)-1)
    elif out<=pow(-2,31):
        out = long(pow(-2,31))
    print(out)