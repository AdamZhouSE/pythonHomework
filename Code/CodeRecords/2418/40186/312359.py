t = int(input())
c = int(input())
x = 0
y = 0
res = [0,0]
for x in range(int(t/4)+1):
    for y in range(int(t/2)+1):
        if x+y==c and x*4+y*2==t:
            res = [x,y]
if res==[0,0] and t!=0:
    print([])
else:
    print(res)