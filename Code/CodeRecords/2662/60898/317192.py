def intToBi(x):
    temp=""
    while(x>1):
        temp=str(x%2)+temp
        x=x//2
    temp=str(x)+temp
    return temp

t=eval(input())
for i in range(0,t):
    x=eval(input())
    str1=intToBi(x)
    cnt=0
    for j in range(0,len(str1)):
        if str1[j]=='1':
            cnt+=1
    if(cnt%2!=0):
        print("odd")
    else:
        print("even")
