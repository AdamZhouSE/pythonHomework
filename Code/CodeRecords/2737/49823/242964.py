def g(l):
    r = list()
    l=sorted(l)
    t = len(l) / 3
    pre = l[0]
    count = 1
    for i in range(1, len(l)):
        if l[i] == pre:
            count += 1
        elif count > t:
            r.append(pre)
            pre = l[i]
            count = 1
        else:
            pre = l[i]
            count = 1
    if count > t:
        r.append(pre)
    print(r)
    
    
if __name__ == '__main__':
    g([int(i) for i in input()[1:-1].split(',')])