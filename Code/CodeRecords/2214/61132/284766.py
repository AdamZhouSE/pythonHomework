a=list(map(int,input().replace('i','').split('+')))
b=list(map(int,input().replace('i','').split('+')))
print(str(a[0]*b[0]-a[1]*b[1])+'+'+str(a[0]*b[1]+a[1]*b[0])+'i')