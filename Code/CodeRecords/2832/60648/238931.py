n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
day=0
m=0
for i in range(n):
    if m<=ls[i]:
        m=ls[i]
    if m==i+1:
        day=day+1
    
    
print(day)