con = [int(i) for i in input().split( )]
n, k = con[0], con[1]
a = input()
b = input()
q = int(input())
while q:
    cmd = [int(i) for i in input().split( )]
    s,t,l,r = cmd[0],cmd[1],cmd[2],cmd[3]
    t = a[s-1:t]
    p = b[l-1:r]
    h = len(p)
    subs = []
    ret = []
    for i in range(len(t)-h+1):
        subs.append(t[i:i+h])
    i = 0
    while i <len(subs):
        if subs[i]==p:
            ret.append(k-i-s)
            i += h-1
        i += 1
    print(sum(ret))
    q -= 1
    