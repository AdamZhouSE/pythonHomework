def power ():
    a = int(input())
    b = input().split()
    c = []
    for i in range(len(b)):
        c.append(int(b[i]))
    c.sort(reverse=True)
    for i in range(len(b)):
        if( c[i] < i+1 ):
            return i

    return a


a = int(input())
for i in range(a):
    print(power())