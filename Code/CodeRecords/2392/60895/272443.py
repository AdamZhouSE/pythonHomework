t=int(input())
while t>0:
    t=t-1
    n,k=input().split(' ')
    n=int(n)
    k=int(k)
    s=input().split(' ')
    result='No'
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])*int(s[j])==k:
                result='Yes'
                break
        if result=='Yes':
            break
    print(result)