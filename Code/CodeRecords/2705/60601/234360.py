def solve(edges):
    tree = ''.join(map(chr, range(1001)))
    for u, v in edges:
        if tree[u] == tree[v]:
            return [u, v]
        tree = tree.replace(tree[u], tree[v])


if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    array = line.split(']')
    M = []
    for i in array:
        if len(i) == 0: continue
        if i[0] == '[':
            i = i[1:len(i)]
        else:
            i = i[3:len(i)]
        i = i.replace(',', ' ')
        i = list(map(int, i.split()))
        M.append(i)
    #print(M)
    print(solve(M))