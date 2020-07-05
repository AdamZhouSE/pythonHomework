f=input()
#print(f)
a=int(f)
f=input()
#print(f)
b=int(f)
f=input()
#print(f)
c=int(f)
sort_abc = sorted([a, b, c])
a, b, c = sort_abc[0], sort_abc[1], sort_abc[2],
# a,b,c位置已经连续
if a+1 == b and b+1 == c:
    print("[0,0]")
else:
    x=1 if (b-a <= 2 or c-b <= 2) else 2
    y=c-a-2
    print([1 if (b-a <= 2 or c-b <= 2) else 2, c-a-2])
