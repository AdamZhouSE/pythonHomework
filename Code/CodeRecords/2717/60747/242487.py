s=input()
equations=s[1:len(s)-1].split(",")
tmp = {chr(i): chr(i) for i in range(97, 125)}


def find(x):
    if x != tmp[x]:
        tmp[x] = find(tmp[x])

    return tmp[x]


for it in equations:

    if it[1] == '=':
        tmp[find(it[0])] = find(it[-1])

for it in equations:

    if it[1] == '!':

        if find(it[0]) == find(it[-1]):
            print( False)
            a=-1
if a!=-1:
    print(True)