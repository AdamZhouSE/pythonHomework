str1=input()
str1=str1[1:len(str1)-1]
list1=list(map(int,str1.split(",")))
k=int(input())
left=0.0
right=1.0
p=0
q=1
len1=len(list1)
while True:
    mid=(left+right)/2
    cnt=0
    p=0
    j=0
    for i in range(0,len1):
        while(j<len1 and list1[i]>mid*list1[j]):
            j=j+1
        cnt=cnt+len1-j
        if j<len1 and p*list1[j]<q*list1[i]:
            p=list1[i]
            q=list1[j]
    if cnt==k:
        break
    elif cnt<k:
        left=mid
    else:
        right=mid
list2=[]
list2.append(p)
list2.append(q)
print(list2)    