# 23
inp = input()
n = int(inp)
need = []
price = []
for i in range(n):
    inp = input()
    nee,p = inp.split()
    need.append(int(nee))
    price.append(int(p))

def f(need,price,ind,su):
    if ind == 0:
        print(su)
        return
    m = min(price[0:ind])
    new_ind = price.index(m)
    all_need = sum(need[new_ind:ind])
    su += all_need*m
    f(need,price,new_ind,su)
        
    
f(need,price,n,0)