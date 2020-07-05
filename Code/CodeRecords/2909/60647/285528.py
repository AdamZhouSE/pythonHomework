str=input()
l=int(input())
a=int(input())
b=int(input())
def count(str,n):
    list=[]
    for i in str:
        if i not in list:
            list.append(i)
    r=len(list)
    if r<=n:
        return True
    else:
        return False
def num(str1,str2):
    n=len(str1)
    res=0
    for i in range(len(str2)-n+1):
        str3=str2[i:i+n]
        if str3==str1:
            res+=1
    return res
res=0
for i in range(a,b+1):
    for j in range(0,len(str)-i+1):
        if count(str[j:j+i],l):
            if num(str[j:j+i],str)>=res:
                res=num(str[j:j+i],str)
print(res)