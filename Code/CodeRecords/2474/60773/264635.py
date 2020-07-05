num=int(input())
for k in range(num):
    s=input()
    left=0
    max=0
    sum=0
    for i in range(len(s)):
        if s[i]=='(':
            left=left+1
        else:
            if left>0:
                left=left-1
                sum=sum+2
                if sum>max:
                    max=sum
            else:
                sum=0
    print(max)