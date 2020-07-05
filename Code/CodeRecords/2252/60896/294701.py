def judge(str1,str2):
    str1.sort()
    str2.sort()
    return(str1==str2)
    

a=eval(input())
for i in range(0,a):
    n=input()
    len1=len(n)
    list1=list(n)
    s=input()
    len2=len(s)
    list2=list(s)
    count=0
    for i in range(0,len1-len2+1):
        if(judge(list1[i:i+len2],list2)):
            count+=1
    print(count)