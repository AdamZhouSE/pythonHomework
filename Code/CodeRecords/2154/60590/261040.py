num = input()
lists = list(num)
lists.reverse()
str = ""
for i in range(lists.__len__()):
    str += lists[i]
print(num == str)
