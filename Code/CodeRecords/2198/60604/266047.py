n=int(input())
s=input()
num=input().split()
tmp=[]
for i in range(0,n):
    tmp.append(s[i:n])
print(tmp)