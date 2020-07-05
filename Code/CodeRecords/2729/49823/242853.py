def f(l):
    r=l[0]
    for i in range(1,len(l)):
        r^=l[i]
    print(r)

if __name__=='__main__':
    l=list()
    #while
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    l.append(int(input()))
    f(l)