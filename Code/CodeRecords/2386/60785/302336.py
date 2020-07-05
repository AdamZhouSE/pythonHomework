t= int(input())
for rfa in range(t):
    n=int(input())
    num=[int(i) for i in input().split()]
    num.sort()
    res=[]
    x= int(input())
    for i in range(n-3):
        for j in range(i+1,n):
            sum=x-num[i]-num[j]
            start=j+1
            end=n-1
            while start<end:
                while start<end and num[start]+num[end]>sum:
                    end-=1
                if(start==end):
                        break;
                if num[start]+num[end]==sum:
                    res.append([num[i],num[j],num[start],num[end]])
                    while start<end and num[start]==num[start+1]:
                        start+=1
                start+=1
            while j<n-1 and num[j]==num[j+1]:
                    j+=1
        while i<n-1 and num[i]==num[i+1]:
                i+=1
                
    if len(res)>0:
        print(1)
    else:
        print(0)