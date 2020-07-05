from fractions import Fraction
dicct = {}
initialList = eval(input())
k = int(input())
length = len(initialList)
Lis = []
for i in range(0,length-1):
    son = initialList[i]
    for j in range(length-1,i,-1):
        mother = initialList[j]
        Lis.append(Fraction(son,mother))

for i in Lis:
    dicct[i] = float(i)
newDict = sorted(dicct.items(),key=lambda item:item[1])
res = newDict[k-1][0]
ans = [res.numerator,res.denominator]
print(ans)
