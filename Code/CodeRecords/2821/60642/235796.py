a = input()
b = input().split(' ')
c = []
p1 = p2 =0

for i in range(len(b)):
    c.append(int(b[i]))

while(len(c)!=0):
    if(c[0]>c[-1]):
        p1=p1+c[0]
        c.pop(0)
    else:
        p1 = p1 + c[-1]
        c.pop(-1)
    if(len(c)==0): break
    if (c[0] > c[-1]):
        p2 = p2 + c[0]
        c.pop(0)
    else:
        p2 = p2 + c[-1]
        c.pop(-1)
    #print(p1, ' ', p2)

print(p1,p2)