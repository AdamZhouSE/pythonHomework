t=int(input())
while t>0:
    t=t-1
    length=int(input())
    s=input().split()
    str=''.join(s)
    result=length
    temp=2
    while temp<=length:
        for i in range(0,length-temp+1):
            string=s[i:i+temp]
            Set=set(string)
            if len(Set)==temp:
                result=result+temp
        temp=temp+1
    print(result)
    