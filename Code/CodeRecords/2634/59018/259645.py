from fractions import Fraction
a1=input()[1:-1].split(',')
a=[int(y) for y in a1]
b=[]
k=int(input())
for j in range(len(a)-1):
    for i in range(j+1,len(a)):
        b.append(Fraction(a[j],a[i]))
b.sort()
print([b[k-1].numerator,b[k-1].denominator])