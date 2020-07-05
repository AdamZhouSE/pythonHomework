strs = input()
lists = list()
for i in range(len(strs)+1):
    lists.append(i)
answer = list()
for i in range(len(strs)):
    if strs[i]=="I":
        temp = lists.pop(0)
        answer.append(temp)
    else:
        temp = lists.pop()
        answer.append(temp)
print(answer)