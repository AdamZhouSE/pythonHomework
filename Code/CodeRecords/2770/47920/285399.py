t = int(input())
for i in range(t):
    length = int(input())
    inp1 = input().split(' ')
    inp2 = input().split(' ')
    s = []
    f = []
    for j in inp1:
        if(j != ''):
            s.append(int(j))
    for k in inp2:
        if(k != ''):
            f.append(int(k))
    print(s)
    print(f)