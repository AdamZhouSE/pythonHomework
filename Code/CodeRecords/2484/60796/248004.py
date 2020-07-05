n=int(input())
result=[]
while n>0:
    num=input().split(" ")
    num=[int(x) for x in num]
    s1=input().split(" ")
    s2=input().split(" ")
    #s1、s2都删除相同的字符
    i=0
    while i<=len(s1)-1:
        a=s1[i]
        while s1.count(a)>1:
            s1.remove(a)
        i=i+1
    
    i=0
    while i<=len(s2)-1:
        a=s2[i]
        while s2.count(a)>1:
            s2.remove(a)
        i=i+1
       
            
    
    str1=","+",".join(s1)+","
    
    i=0
    while i<=len(s2)-1:
        if str1.__contains__(","+s2[i]+","):
            del s2[i]
            i=i-1
        i=i+1
    result.append(len(s1)+len(s2))
    n=n-1

for i in range(0,len(result)):
    print(result[i])
    