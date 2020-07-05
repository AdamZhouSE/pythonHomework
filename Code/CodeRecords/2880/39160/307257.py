n, k = input().split()
n = int(n)
k = int(k)
children = list(map(int, input().split()))

res = 0
while(children):
    if children[0] <= k:
        res+=1
        children.pop(0)
    elif children[-1] <= k:
        res+=1
        children.pop()
    else:
        break
    
        
print(res)