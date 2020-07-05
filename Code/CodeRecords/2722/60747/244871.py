n=int(input())
result=[]
for i in range(n):
    num=input()
    if num[len(num)-1]=='5'or num[len(num)-1]=='0':
        result.append("YES")
    else: result.append("NO")
for i in range(len(result)):
    print(result[i])