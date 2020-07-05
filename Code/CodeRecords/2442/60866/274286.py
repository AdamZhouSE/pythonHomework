def shuzu(a):
    if len(a)<2:
        return 0
    else:
        a.sort()
        num=a[1]-a[0]
        for i in range(1,len(a)-1):
            if a[i+1]-a[i]>num:
                num=a[i+1]-a[i]
        return num
a=eval(input())
print(shuzu(a))