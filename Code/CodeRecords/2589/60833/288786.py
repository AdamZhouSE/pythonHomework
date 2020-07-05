def feiqinabo(s):
    if(s==0):
        return 2
    elif(s==1):
        return 1
    else:
        return feiqinabo(s-1)+feiqinabo(s-2)
n=int(input())
for i in range(0,n):
    s=int(input())
    print(feiqinabo(s))