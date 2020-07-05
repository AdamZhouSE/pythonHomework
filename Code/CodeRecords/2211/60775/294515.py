input1 = input().split(' ')
n_wife = int(input1[0])
n_que = int(input1[1])

names = ['']
for i in range(1,n_wife+1):
    inpu2 = input().split(' ')
    first = inpu2[0]
    mon = int(inpu2[1])
    names.append(first + names[mon])

for q in range(n_que):
    result = 0
    query = input()
    for name in names:
        if name.startswith(query):
            result += 1
    print(result)