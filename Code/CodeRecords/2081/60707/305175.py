
ss = input()
str1 = input()
count = 0
for i in range(len(ss)):
    for j in range(i, len(ss) + 1):
        if ss[i:(j + 1)] == str1:
            count += 1
if count == 2:
    print("1",end="")
else:
    print(str(count),end="")
