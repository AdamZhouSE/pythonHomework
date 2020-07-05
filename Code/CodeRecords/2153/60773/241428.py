s=str(input())
n=len(s)
result=""
if s[0]=='-':
    for i in range(1,n,1):
        result=s[i]+result
    result="-"+result
    num = int(result)
    print(num)

else:
    for i in s:
        result=i+result
    num=int(result)
    print(num)