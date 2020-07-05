n=int(input())
result=[]
str=[]
for i in range(n):
    s=input()
    str=[]
    for j in s:
        str.append(j)
    result.append(len(set(str)))
for k in range(n):
    print(result[k])