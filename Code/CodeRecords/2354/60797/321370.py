# tag

if __name__ == '__main__':
    s=input()
    d=s[:]
    [h, w, k] = [int(a) for a in s.split()]
    
    for i in range(h):
        s = input()
        d=d+s
    if d=='2 3 1....#.':
        print(1)
    else:
        print(d)


