n = eval(input())
n.sort()
if len(n)<2:
    print(0)
else:
    res = 0
    for i in range(0,len(n)-1):
        if n[i+1]-n[i]>res:
            res = n[i+1]-n[i]
    print(res)