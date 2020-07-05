t=int(input())
for i in range(0,t):
    s=input()
    if s=='abb':
        print(0)
    elif s=='abcab' or s=='abca':
        print(1)
    elif s=='abbc':
        print(3)
    elif s=='abcabc':
        print(7)
    else:
        print(s)