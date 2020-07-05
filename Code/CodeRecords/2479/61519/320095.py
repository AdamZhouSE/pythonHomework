n=int(input())
for i in range(n):
    res=""
    num1=list(input())
    num2=list(input())
    for j in num1:
        if j not in num2 and j not in res:
            res=res+j
    for j in num2:
        if j not in num1 and j not in res:
            res=res+j
    tem=list(res)
    tem.sort()
    res="".join(tem)
    print(res,end="\n\n")