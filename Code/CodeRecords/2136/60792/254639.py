def judge(n,k):
    str1=""
    while n>0:
        rem=n%k
        n=n//k
        str1=str(rem)+str1
    flag=True
    for i in range(0,len(str1)):
        if(str1[i]!="1"):
            flag=False
            break
    return flag

n=int(input())
k=2
while not(judge(n,k)):
    k=k+1
print(k)
