x1,y1=map(int,input()[:-1].split("+"))
x2,y2=map(int,input()[:-1].split("+"))
x3=x1*x2-y1*y2
y3=y1*x2+x1*y2
print("%d+%di" %(x3,y3))