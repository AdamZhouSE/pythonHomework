a=int(input())
for k in range(0,a):
    a=input().split(' ')
    qi=int(a[0])
    weishu=int(a[1])
    str=""
    for i in range(0,weishu):
        str=str+"1"
    result=int(str,2)-qi+1
    print(result)