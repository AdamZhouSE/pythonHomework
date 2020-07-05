# 1
inp = input()
n = int(inp)
dot = []
for i in range(n):
    inp = input()
    x,y = inp.split(',')
    x = int(x)
    y = int(y)
    dot.append([x,y])

def square(d1,d2,d3):
    x1,y1= d1
    x2,y2= d2
    x3,y3= d3
    return (1/2)*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    
max_s = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i:
                s = square(dot[i],dot[j],dot[k])
                if s>max_s:
                    max_s = s
print(max_s)