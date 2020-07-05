def shuzu(a):
    ans=0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>2*a[j]:
                ans=ans+1
    return ans
a=eval(input())
print(shuzu(a))