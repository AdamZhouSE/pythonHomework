points=eval(input())
k=int(input())
def s(x,y):
    return(x**2+y**2)
result=sorted(points,key=lambda k:s(k[0],k[1]))
print(result[:k])