n = int(input())

for i in range(0,n):
    e=int(input())
    s=0
    for j in range(1,e+1):
        s+=j**5
    print(s)    