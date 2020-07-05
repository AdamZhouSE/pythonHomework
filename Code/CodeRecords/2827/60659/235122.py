n=int(input())
num=input().split(" ")
for j in range(n):
    num[j]=int(num[j])
num.sort()
result=""
for x in num:
    result+=str(x)
    result+=" "
print(result[0:len(result)-1])