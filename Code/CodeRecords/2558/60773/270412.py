num=int(input())
for k in range(num):
    s=input()
    n=len(s)
    left=0
    sum=0
    if n%2!=0:
        print(-1)
    else:
        for i in range(n):
            if s[i]=='{':
                left=left+1
            else:
                if left>0:
                    left=left-1
                else:
                    left=left+1
                    sum=sum+1
    
        sum=sum+left//2
        print(sum)