def calculate(p,t,r):
    return (int)(p*t*r/100)
tests=(int)(input())
for i in range(tests):
    p=(int)(input())
    t=(int)(input())
    r=(int)(input())
    print(calculate(p,t,r))