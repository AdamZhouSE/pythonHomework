a=float(input())
b=int(input())
re=1.00000
if b>=0:
    for i in range(0,b):
        re*=a
    print("%.5f"%re)
else:
    for i in range(0,-b):
        re*=a
    print("%.5f"%(1/re))