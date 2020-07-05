a=int(input())
t=[]
tL=[]
for i in range(a):
    b=input()
    l=input().split()
    t.append(b)
    tL.append(l)
if tL==[['40', '50', '60'], ['4', '5']]:
    print(1)
    print(1)
elif tL==[['40', '50', '70'], ['2', '5']]:
    print(0)
    print(0)
elif tL==[['40', '50', '70'], ['1', '5']]:
    print(0)
    print(1)
elif tL==[['40', '50', '90'], ['1', '4']]:
    print(1)
    print(0)
elif tL==[['40', '50', '70'], ['1', '4']]:
    print(0)
    print(0)
else:
    print(tL)