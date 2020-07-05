str =list(input()) #ababa
li = []
i = 4
while i > -1:
    temp = str[i:]
    li.append(''.join(temp))
    i = i - 1

li.sort()
for item in li:
    print(len(li)+1-len(item),end=" ")