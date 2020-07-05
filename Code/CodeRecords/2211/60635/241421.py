infos = [int(x) for x in input().split()]
madams = []
interest = {}
repo=[]
for i in range(infos[0]):
    tmp = input().split()
    madams.append((tmp[0], int(tmp[1])))
for i in range(infos[1]):
    tmp=input()
    interest[tmp] = 0
    repo.append(tmp)

def find(s, i):
    if len(s) == 0 :
        return ''
    if i == 0:
        return madams[i][0]
    return madams[i][0]+find(s[1:], madams[i][1]-1)


for s in interest:
    for i in range(infos[0]):
        if madams[i][0] == s[0]:
            if find(s, i) == s:
                interest[s] += 1
ans = [str(interest[x]) for x in repo]
print('\n'.join(ans))