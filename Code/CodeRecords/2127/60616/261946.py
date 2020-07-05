def superPow(a, b) :
    r = 1
    for _b in b:
        r = pow(r, 10, 1337) * pow(a, _b, 1337) % 1337
    return r
a=int(input())
rawInput=input().split(',')
items=[]
for item in rawInput:items.append(int(item))
print(superPow(a,items))