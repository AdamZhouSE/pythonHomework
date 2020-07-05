def circularPermutation(n, start):
    if n <= 0:
        return []
    if start >= 2**n:
        return []
    
    res = ['0', '1']
    walk(n, res, 1)
    res = list(map(lambda a: int(a, 2), res))
    idx = res.index(start)
    return res[idx:]+res[:idx]
    
def walk(n, res, start):
    
    if start == n:
        return
    
    temp = []
    while res:
        temp.append(res.pop(0))
        
    for i in temp:
        res.append('0'+i)
        
    for i in temp[::-1]:
        res.append('1'+i)
    
    start+=1
    
    
    walk(n, res, start)
    return

n=int(input())
start=int(input())
print(circularPermutation(n, start))