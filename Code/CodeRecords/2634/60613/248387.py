from fractions import Fraction

string=input()
NUM=int(input())
standard=list(map(int,string[1:len(string)-1].split(",")))

lst=[]
for i in range(len(standard)-1):
    for j in range(i+1,len(standard)):
        lst.append(Fraction(standard[i],standard[j]))
lst.sort()
result=lst[NUM-1]
result999=[]
for i in range(len(standard)-1):
    for j in range(i+1,len(standard)):
        if Fraction(standard[i],standard[j])==result:
            result999=[standard[i],standard[j]]
            break
    if len(result999)==2:
        break
print(result999)

