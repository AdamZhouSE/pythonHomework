n=int(input())
result=[]
while n>0:
    s=input()
    s1=input().split(" ")
    s1=[int(x) for x in s1]
    s2=input().split(" ")
    s2=[int(x) for x in s2]
    max=(len(s1)-1)+(len(s2)-1)
    this=""
    for i in range(max+1):
        coef=0#系数
        for j in range(len(s1)):
            for k in range(len(s2)):
                if j+k==i:
                    coef=coef+s1[j]*s2[k]
        this=this+str(coef)+" "
    this=this[:len(this)-1]
    result.append(this)
    n=n-1


for i in range(0,len(result)):
    print(result[i])