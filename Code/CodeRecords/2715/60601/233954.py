
def solve(stones):
    UF = {}

    def find(x):
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        UF.setdefault(x, x)
        UF.setdefault(y, y)
        UF[find(x)] = find(y)

    for i, j in stones:
        union(i, ~j)
    return len(stones) - len({find(x) for x in UF})

if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    array = line.split(']')
    M =[]
    for i in array:
        if len(i)==0:continue
        if i[0]=='[':
            i = i[1:len(i)]
        else: i = i[2:len(i)]
        i = i.replace(',',' ')
        i = list(map(int,i.split()))
        M.append(i)
    #print(M)
    print(solve(M))