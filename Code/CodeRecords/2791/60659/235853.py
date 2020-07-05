n=int(input())
num=input().split()
for i in range(n):
    num[i]=int(num[i])
result=0
number=""
for j in range(n):
    if num[j]==1:
        result+=1
    if j+1<n and num[j+1]==1:
        number+=str(num[j])
        number+=" "
number+=str(num[n-1])
print(result)
print(number)