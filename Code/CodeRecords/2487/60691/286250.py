def vote(s):
    l = s.split(' ')

    string = []
    for i in range(len(l)):
        if not l[i] in string:
            string.append(l[i])

    storage = [[]for i in range(len(string))]
    for i in range(len(string)):
        storage[i].append(string[i])
        storage[i].append(l.count(string[i]))

    storage.sort(key=lambda x: x[1], reverse=True)
    print(storage[0][0]+' '+str(storage[0][1]))


n = int(input())
nums = []
strlist = []
for i in range(n):
    nums.append(input())
    strlist.append(input())

for i in range(n):
    vote(strlist[i])

