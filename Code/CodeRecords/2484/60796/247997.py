n=int(input())
result=[]
while n>0:
    num=input().split(" ")
    num=[int(x) for x in num]
    s1=input().split(" ")
    s2=input().split(" ")
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
    