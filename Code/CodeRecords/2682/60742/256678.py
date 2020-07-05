t = int(input())
for k in range(t):
    n,l,r = [int(i) for i in input().split()]
    help = []
    for i in range(1,r+1):
        if i<l:
            help.append('0')
        else:
            help.append('1')
    help.reverse()
    help.insert(0,'0')
    help_int = int(''.join(help),2)
    res = n | help_int
    print(res)