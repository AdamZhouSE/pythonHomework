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
                temp0=s[j:j+i]
                if temp0==temp:
                    result=result-1
                    break
        print(result)
        len=len+1