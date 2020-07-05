def count(list1,n,m):
    str1=list1[n]
    str2=list1[m]
    counts=0
    j=0
    for i in range(0,len(str2)):
        if j<len(str1) and str1[j]!=str2[i]:
            j=0
        else:
            if j==len(str1)-1:
                counts=counts+1
                j=0
            else:
                j=j+1
    return counts

s=input()
list1=[]
temp=""
for i in range(0,len(s)):
    if s[i]=="P":
        list1.append(temp)
    elif s[i]=="B":
        temp=temp[0:len(temp)-1]
    else:
        temp=temp+s[i]
m=int(input())
for i in range(0,m):
    n,m=map(int,input().split(" "))
    if m-1>len(list1)-1:
        print(0)
    else:
        print(count(list1,n-1,m-1))
    