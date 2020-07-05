def find(l,n2):
    n1=len(l)
    for i in range(n1):
        sum=0
        for j in range(i,n1,1):
            sum=sum+int(l2[j])
            if(sum==n2):
                result=str(i+1)+" "+str(j+1)
                return result
    return "-1"

num=int(input())
for k in range(num):
    l1=input().split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    l2=input().split(" ")
    str1=find(l2,n2)
    print(str1)
