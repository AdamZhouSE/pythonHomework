t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    temp1=''
    temp2=''
    for item in s:
        if int(item)==0:
            temp2=temp2+'0'+' '
        else:
            temp1=temp1+item+' '
    result=temp1+temp2
    print(result)