def shuzi(a):
    num=[]
    for i in range(0,a):
        num.append(0)
    count=0
    for i in range(2,a):
        if num[i]==0:
            count=count+1
            j=i+i
            while j<a:
                num[j]=1
                j=j+i
    return count
a=int(input())
print(shuzi(a))