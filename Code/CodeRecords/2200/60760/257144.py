str0=input()
str1=input()
k=int(input())
result = []
result2=[]
length=len(str0)
for j in range(1, length + 1):
    for n in range(length - j + 1):
        son = str0[n:n + j]
        result.append(son)
        result2.append(str1[n:n+j])
#result2=list(set(result2))
#result=list(set(result))
#print(result)
#print(result2)
result4=[]
for i in range(len(result2)):
    if len(result2[i])-result2[i].count("1")<=k:
        result4.append(result2[i])
print(len(set(result4)))