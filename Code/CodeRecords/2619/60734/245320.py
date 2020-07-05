def lucky(x):
    res = []
    for i in range(len(x)):
        for j in range(i+1,len(x)+1):
            res.append(x[i:j])
    for i in range(len(res)):
        lst = list(map(int,res[i]))
        a = 1
        for k in lst:
            a*=k
        res[i] = a
    return repeat(res)

def repeat(res):
    res.sort()
    for i in range(1,len(res)):
        if res[i-1] == res[i]:
            return 0
    return 1
        
    
     
t = int(input())
res = []
for i in range(t):
    res.append(lucky(input()))
for x in res:
    print(x)