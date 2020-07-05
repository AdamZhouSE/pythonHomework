def trans(num):
    dividend=num
    result=''
    while dividend!=0:
        remainder=dividend%2
        result=str(remainder)+result
        dividend=dividend//2
    return result

t=int(input())
for i in range(t):
    n=int(input())
    result=''
    for j in range(1,n+1):
        result+=trans(j)+' '
    print(result)