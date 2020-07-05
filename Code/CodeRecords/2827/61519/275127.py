n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort()
for i in range(n):
    num[i]=str(num[i])
string=" ".join(num)
print(string)