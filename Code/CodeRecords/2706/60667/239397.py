accounts = eval(input())
emails = []
names = []
result = []
for i in range(len(accounts)):
    emails.append(accounts[i][1:])
    names.append(accounts[i][0])
for i in range(len(emails)):
    for j in emails[i]:
        for k in emails[i+1:]:
            if j in k:
                emails[i] = emails[i] + k
                continue

length = len(emails)
pointer = 0
while pointer < length:
    for j in emails[:pointer]+emails[pointer+1:]:
        if set(j).issubset(emails[pointer]):
            names.remove(names[emails.index(j)])
            emails.remove(j)
            length = length - 1
    if pointer < length:
        pointer = pointer + 1

for i in range(len(emails)):
    result.append([])

for i in range(len(emails)):
    result[i].append(names[i])
    for j in range(len(emails[i])):
        if emails[i][j] not in result[i]:
            result[i].append(emails[i][j])

print(result)