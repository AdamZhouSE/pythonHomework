n=int(input())
for i in range(0,n):
    s=input()
    max_val=-1
    for i in range(0,len(s)):
        for j in range(len(s)-1,i,-1):
            if(s[j]==s[i]):
                max_val=max(max_val,j-i-1)
    print(max_val)