a=list(map(int,input().split(',')))
result=[[]]
num=[]
for i in range(len(a)):
    for j in range(len(result)):
        result.append(result[j]+[a[i]])
result.remove([])
for i in range(len(result)):
    num.append(max(result[i])-min(result[i]))
print(sum(num))