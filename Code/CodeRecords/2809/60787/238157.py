n=int(input())
stick=[int(i) for i in input().split()]
stick=sorted(stick)
a,b=0,0
for i in range(0,int(n/2)):
    a+=stick[i]
for i in range(int(n/2),n):
    b+=stick[i]
print(a*a+b*b)