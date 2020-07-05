T = int(input())
for i in range(T):
    s = (''+input()).split(' ')
    s =  list(map(int,s))
    n = s[0]
    m = s[1]
    x = s[2]
    A = ('' + input()).split(' ')
    B = ('' + input()).split(' ')
    # A = list(map(int,(''+input()).split(' ')))
    # B = list(map(int,(''+input()).split(' ')))
    for i in A:
        if str(x-int(i)) in B:
            print(i,str(x-int(i)))