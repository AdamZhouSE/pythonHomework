record=int(input())
result=[0for k in range(20)]
for i in range(record):
    s=input().split(",")
    for j in range(3):
        s[j]=int(s[j])
    for l in range(s[0],s[1]+1):
        result[l-1]+=s[2]
n=int(input())
f_result=[]
for h in range(n):
    f_result.append(result[h])
print(f_result)