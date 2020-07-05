import re

s = input()
ls = []
while s != "":
    try:
        ls.append(s)
        s = input()
    except EOFError:
        break
i=0
result=[]
while i<=len(ls)-2:
    pattern = "^"+ls[i]+"$"
    s = ls[i+1]

    if re.match(pattern, s) != None:
        result.append("Yes")

    else:
        result.append("No")
    i=i+2

for i in range(len(result)):
    print(result[i])