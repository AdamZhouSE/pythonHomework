num = int(input())
str = str(num)
lists = list(str)
lists.reverse()
res=""
for i in range(lists.__len__()):
    res+=lists[i]
print(res)