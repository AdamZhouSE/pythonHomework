def el(l):
    l.sort()
    if len(set(l))!=2 or len(set(l))!=3 or l[2]!=l[3] or (len(set(l[0:4]))!=1 and len(set(l[1:5]))!=1 and len(set(l[2:6]))!=1):
        print('Alien')
        return
    if len(set(l))==2:
        print('Elephant')
        return
    print('Bear')
if __name__ == '__main__':
    el([int(i) for i in input().split(' ')])
