list1=list(input())
list1=[int(list1[i]) for i in range(len(list1))]
maxn=list1[1]
index=1
for i in range(2,len(list1)):
    if maxn<list1[i]:
        maxn=list1[i]
        index=i
if list1[0]<maxn:
    list1[index]=list1[0]
    list1[0]=maxn
list1=[str(list1[i]) for i in range(len(list1))]
str1=''.join(list1)
print(str1)