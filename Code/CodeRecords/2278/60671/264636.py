time=int(input())
length=int(input())
str1=input()
list0=str1.split()
listnum=[]
for x in list0:
    listnum.append(int(x))
new=[]
for i in range(length-1):
    new.append(listnum[i]^listnum[i+1])

new.append(listnum[-1])

print(*new)
         