n=int(input())
s=input().split(' ')
result=0
length=1
while length<=n:
    if length==1:
        result=1
        print(result)
        length=length+1
    else:
        result=result+length
        for i in range(1,length):
            temp=s[length-i:length]
            for j in range(0,length-i):
                temp1=s[j:j+i]
                if temp==temp1:
                    result=result-1
                    break
        print(result)
        length=length+1