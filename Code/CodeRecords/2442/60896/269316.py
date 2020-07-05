a=eval(input())
maxnum=0
if(len(a)<2):
    print(maxnum)
else:
    a.sort()
    for i in range(1,len(a)):
        temp=a[i]-a[i-1]
        maxnum=max(temp,maxnum)
    print(maxnum)
        