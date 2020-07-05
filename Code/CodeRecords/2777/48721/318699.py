t = int(input())
for i in range(t):
    n = int(input())
    inp = input().split(' ')
    temp = []
    for i in inp:
        temp.append(int(i))
    temp = sorted(temp)
    if(n % 2 == 1):
        t = int(n/2)
        print(temp[t])
    else:
        tm  = int(n/2)
        sm = temp[tm-1] + temp[tm]
        print(int(sm/2))