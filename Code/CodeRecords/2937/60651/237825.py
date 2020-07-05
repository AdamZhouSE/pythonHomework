list1=list(input())
n=len(list1)
sum=0
list0=list("CODEFESTIVAL2016")
list0=[ord(x) for x in list0]
list1=[ord(x) for x in list1]
for i in range(n):
    list1[i]=list1[i]-list0[i]
for i in range(n):
    if list1[i]!=0:
        sum+=1
print(sum)    