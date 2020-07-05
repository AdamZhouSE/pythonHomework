x = input().strip().split()
n = int(x[0])
q = int(x[1])
fatherli = [-1 for i in range(n)]
tagli = [False for ii in range(n)]

for i in range(n-1):
    x = input().strip().split()
    u = int(x[0])-1
    v = int(x[1])-1
    fatherli[v] = u

tagli[0] = True

for i in range(q):
    x = input().strip().split()
    if x[0] == "C":
        tagli[int(x[1])-1] = True
    else:
        # 寻找最近的被标记的
        curr = int(x[1])-1
        fa = curr
        while not tagli[fa]:
            fa = fatherli[fa]
        print(fa+1)