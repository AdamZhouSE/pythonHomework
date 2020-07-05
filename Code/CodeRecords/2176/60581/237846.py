str = list(input())
li = []
i = len(str) - 1
while i > -1:
    temp = str[1:]
    li.append(''.join(temp))
    i = i - 1

li.sort()
result = []
for item in li:
    result.append(len(li)+1-len(item))

j = 0
while j < len(result)-1:
    print(result[j],end=" ")
    j = j+1
print(result[-1])