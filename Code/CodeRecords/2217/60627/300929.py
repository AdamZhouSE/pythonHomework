a = eval('['+input()+']')
b = eval('['+input()+']')
c = eval('['+input()+']')
d = eval('['+input()+']')

def f(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2
print(f(a,b),f(a,c),f(a,d))