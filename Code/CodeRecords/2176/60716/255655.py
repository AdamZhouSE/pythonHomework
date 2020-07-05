string = input()
dicts = dict()
lists = list()
for i in range(len(string)):
    temp = string[len(string)-i-1:]
    dicts[temp]=len(string)-i-1
    lists.append(temp)
lists.sort()
answer = list()
for i in range(len(lists)):
    answer.append(dicts[lists[i]])
strs = [str(i) for i in answer]
strss = ' '.join(strs)
print(strss,end='')