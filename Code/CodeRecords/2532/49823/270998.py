def au(l):
    ll=sorted(l)
    d=0
    for i in range(len(l)):
        d+=1 if l[i]==ll[i] else 0
    print(d)
if __name__ == '__main__':
    au(eval(input()))
