s=input().split(" ")
n=int(s[0])
k=int(s[1])
count=0
num=input().split(" ")
for i in range(n):
    if num[i].count('4')+num[i].count("7")<=k:
        count+=1
print(count)