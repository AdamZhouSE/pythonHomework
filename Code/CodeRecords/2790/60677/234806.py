def fun(a,b):
    sum=0
    for i in a:
        if i<=b:
            sum+=1
    return str(sum)

str1=input().split()
str2=input().split()
str3=input().split()
par1=[int(x) for x in str1]
par2=[int(x) for x in str2]
par3=[int(x) for x in str3]
answer=[]
for i in range(par1[1]):
    answer.append(fun(par2,par3[i]))
print(' '.join(answer))