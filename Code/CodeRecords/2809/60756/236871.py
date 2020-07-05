firstLine=input()
n=int(firstLine)
secondLine=input().split()
secondLine.sort(key=int)
half=((n-1)//2)
if n%2==0:
    half+=1
sum1=0
sum2=0
for i in range(half):
    sum1+=int(secondLine[i])
for i in range(half,n):
    sum2+=int(secondLine[i])
print(sum1*sum1+sum2*sum2)