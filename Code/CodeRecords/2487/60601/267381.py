n = eval(input())
for i in range(n):
    m = eval(input())
    name = input().split(' ')
    Lname = list(set(name))
    re = []
    for i in Lname:
        re.append([i,name.count(i)])
    re.sort(key=lambda x:(-x[1],x))
    print(' '.join(map(str,re[0])))