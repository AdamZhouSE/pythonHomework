import sys
n, root = list(map(int, sys.stdin.readline().split()))
tree = {}
for i in range(n):
    fa, lch, rch = list(map(int, sys.stdin.readline().split()))
    tree[lch] = fa
    tree[rch] = fa
m = int(sys.stdin.readline())
result = {}
def find(tree, a, b):
    # if "/".join([str(min(a,b)),str(max(a,b))]) in result:
    #     return result["/".join([str(min(a,b)), str(max(a,b))])]
    # else:
    ld = 0
    lpath = [a]
    la = a
    while la!=root:
        la = tree[la]
        ld+=1
    rd = 0
    rpath = [b]
    lb = b
    while lb!=root:
        lb = tree[lb]
        rd+=1
    if ld>rd:
        dd = ld-rd
        while dd>0:
            a = tree[a]
            lpath.append(a)
            dd-=1
    elif ld<rd:
        dd = rd - ld
        while dd>0:
            b = tree[b]
            rpath.append(b)
            dd-=1
    while a!=b:
        a = tree[a]
        b = tree[b]
        lpath.append(a)
        rpath.append(b)
        # for elea in lpath:
        #     for eleb in rpath:
        #         result['/'.join([str(min(elea,eleb)), str(max(elea,eleb))])] = a
    return a
for i in range(m):
    o1, o2 = list(map(int, sys.stdin.readline().split()))
    print(find(tree, o1, o2))