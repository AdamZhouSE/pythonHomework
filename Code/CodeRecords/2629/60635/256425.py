cases=int(input())
req=[]
for i in range(cases):
    req=int(input())
    print(bin(req).count('1'))
    