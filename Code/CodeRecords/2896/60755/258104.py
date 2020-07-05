newspaper = list(input().replace(" ", ""))
kill = list(input().replace(" ", ""))
flag = 1
for i in kill:
    if newspaper.count(i) != 0:
        newspaper.remove(i)
    else:
        flag = 0
        break
if flag:
    print("YES",end="")
else:
    print("NO",end="")