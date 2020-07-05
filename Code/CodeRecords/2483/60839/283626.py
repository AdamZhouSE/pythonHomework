def func(str1,str2):
    str11=list(str1)
    str22=set(str2)
    for i in range(0,len(str11)):
        if str11[i] in str22:
            return str11[i]
    return "$"


n=int(input())
ans=[]
for i in range(0,n):
    ans.append(func(input(),input()))

for i in range(0,n):
    print(ans[i])