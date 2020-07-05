n=int(input())
num_list=list(map(int,input().split(" ")))
answer=False
Output="Yes"
def test(a,b):
    for i in range(10):
        for j in range(10):
            if a*2**i==b*3**j or a*3**i==b*2**j:
                return True
    return False   
        
def Judge(a,b):
    if a==b:
        return True
    c=max(a,b)
    d=min(a,b)
    if test(a,b):
        return True
    if c%d==0:
        return True
    e=c/d
    while True:
        if e%3==0:
            e=e/3
            continue
        elif e==1:
            return True
        else:
            if e%2==0:
                e=e/2
                continue
    return False
for j in range(n):
    if not Judge(num_list[0],num_list[j]):
        Output="No"
        break
print(Output)

        
        