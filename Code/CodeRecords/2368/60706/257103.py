t=int(input())
for i in range(t):
    n=int(input())
    list4=input().split()
    count=len(list4)
    for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
    num=[]
    m=0
    n=len(list4)-1
    while n>int(len(list4)/2)-1:
        if n==m:
            num.append(list4[n])
        else:
            num.append(list4[n])
            num.append(list4[m])
        n=n-1
        m=m+1
    str1=''
    for i in range(len(num)-1):
        str1=str1+num[i]+' '
    str1=str1+num[len(num)-1]
    print(str1)
        
        