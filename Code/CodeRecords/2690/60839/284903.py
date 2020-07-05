def recursive(num,str1,str2) -> int:
    temp=0
    for i in range(0,len(str1)):
        if (str1[i]==str2[0])&(len(str2)!=1)&(len(str1)>=len(str2)):
            num=recursive(num,str1[i+1:],str2[1:])
        if (len(str2)==1)&(str1[i]==str2[0]):
            temp=temp+1
    return num+temp

def func(lis):
    s1=lis[0]
    s2=lis[1]
    list1=list(s1)
    list2=list(s2)
    temp=[]
    tem=""
    for i in range(0,len(list1)):
        if list1[i] in list2:
            temp.append(list1[i])
            tem=tem+str(list1[i])
    #gksgks    gks
    ans=0
    for i in range(0,len(tem)):
        if  (temp[i]==list2[0])&(len(list2)!=1):
            ans=recursive(ans,tem[i+1:],s2[1:])
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    input()
    s=input().split(" ")
    ans.append(func(s))

for i in ans:
    print(i)