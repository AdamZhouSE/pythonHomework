a1,b1=map(int,input().replace('i','').split('+'))
a2,b2=map(int,input().replace('i','').split('+'))
a=a1*a2-b1*b2
b=a1*b2+a2*b1
print(str(a)+'+'+str(b)+'i')