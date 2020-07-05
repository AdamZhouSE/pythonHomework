str1=input()
list1=[]
n=int(input())
count=0
for i in range(0,n):
    list1.append(input())
for i in range(0,len(str1)-7):
    tmp1=list(str1[i:i+8])
    tmp1.sort()
    for j in list1:
        tmp2=list(j)
        tmp2.sort()
        if tmp2==tmp1:
            count+=1
print(count)