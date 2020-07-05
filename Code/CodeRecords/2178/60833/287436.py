n=int(input())
s=input().split(' ')
result=0
len=1
while len<=n:
    if len==1:
        result=1
        print(result)
        len=len+1
    else:
        result=result+len
        for i in range(1,len):
            temp=s[len-i:len]
            for j in range(0,len-i):
                temp1=s[j:j+1]
                if temp==temp1:
                    result=result-1
                    break
        print(result)
        len=len+1