num=int(input())
s=input().split(' ')
s=list(map(int,s))
sum=0
for i in range(1,len(s)-1):
    if(s[i]>s[i+1] and s[i]>s[i-1]):
        sum+=1
    else:
        if (s[i] < s[i - 1] and s[i] < s[i + 1]):
            sum+=1
print(sum)