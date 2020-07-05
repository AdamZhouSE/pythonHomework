N=int(input())
for n in range(0,N):
    str=input()
    list=[]
    k=-1
    for item in str:
        if item.isdigit():
            k=k+1
            list.append(int(item))
        else:
            b=list[k]
            a=list[k-1]
            c=0
            if item=='+':
                c=a+b
            elif item=='-':
                c=a-b
            elif item=='*':
                c=a*b
            else:
                c=a/b
            list.pop(k)
            list.pop(k-1)
            list.append(c)
            k=k-1
    print(list[0])

