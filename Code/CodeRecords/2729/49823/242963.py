def f(l):
    r=int(l[0])
    for i in range(1,len(l)):
        r^=int(l[i])
    print(r)

if __name__=='__main__':
    f(input()[1:-1].split(','))