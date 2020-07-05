def f(x):
    lst = []
    while x>0:
        lst.append(x&1)
        x = x>>1
    if lst.count(1)>1:
        return -1
    else:
        return lst.index(1)+1
    
t = int(input())
for i in range(t):
    print(f(int(input())))