n=int(input())
num=[0for j in range(50)]
for i in range(n):
    s=input().split(" ")
    for k in range(int(s[0]),int(s[1])):
        if num[k]<int(s[2]):
            num[k]=int(s[2])
print(sum(num))