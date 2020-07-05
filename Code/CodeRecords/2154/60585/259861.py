num=input()
n=len(num)
i=0
j=n-1
isR=True
while i<j:
    if num[i]!=num[j]:
        isR=False
        break
    i+=1
    j-=1
print(isR)