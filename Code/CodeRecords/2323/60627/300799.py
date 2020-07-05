a = eval('['+input() + ']')
k = int(input())
if max(a)-min(a)>2*k:
    print(max(a)-min(a)-2*k)
else:
    print(0)