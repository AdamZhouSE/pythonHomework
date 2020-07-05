def al(a,b):
    s=set()
    for i in b:
        s.add(i)
    r=0
    while True:
        if s==set(a):
            print(r)
            return
        r+=1
        for i in b:
            if i+r in a:
                s.add(i+r)
            if i-r in a:
                s.add(i-r)
    print(r)
if __name__ == '__main__':
    al([int(i) for i in input().split(',')],[int(i) for  i in input().split(',')])
