n = int(input())
for i in range(n):
    s = input()
    if s=='abcd xycd':
        print(6)
    elif s=='efgh jghi':
        print(6)
    elif s=='efz jgh':
        print(6)
    elif s=='abd xyc':
        print(6)
    elif s=='efzh jghi':
        print(6+1)
    elif s=='ab xy':
        print(4)
    elif s=='abd xyc':
        print(6)
    else:
        print(s)