n=int(input())
namelist=[]
current=[]
for i in range(0,n):
    namelist.append(input())
m=int(input())
for i in range(0,m):
    s=input()
    if s in current:
        print("REPEAT")
    elif s in namelist:
        print("OK")
        current.append(s)
    elif s not in namelist:
        print("WRONG")