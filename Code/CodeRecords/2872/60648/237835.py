n=input()
n=int(n)
s=input()
ls=[]
count=0
for i in range(n):
    ls.append(s[i])
'''
for i in range(n):
    print(ls[i])
'''
for j=1 in range(n):
    if ls[j]==ls[j-1]:
        count=count+1
print(count)