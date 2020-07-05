s=list(eval(input()))
count=0
low=int(input())
high=int(input())
for i in range(len(s)):
    for k in range(i,len(s)):
        sum=0
        d=i
        while 1 :
            sum+=s[d]
            if(d==k):break
            d += 1
        if(sum>=low and sum<=high):count+=1
print(count)
