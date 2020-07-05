text = input()
lists = list(text)
#print(lists)

res = 0
for i in range(lists.__len__()):
    if lists[i] == ' ' or lists[i] == '\n':
        continue
    else:
        res+=1;
print(res, end="")