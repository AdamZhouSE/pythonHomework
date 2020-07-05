n=int(input())
str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
l=[0]*n
for i in range(n):
    a=str1[i]
    l[a-1]=str(i+1)
res=' '.join(l)
print(res)