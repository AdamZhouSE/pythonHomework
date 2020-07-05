t=int(input())
for i in range(t):
    n=int(input())
    list4=input().split(' ')
    num1=[]
    for i in range(1,len(list4)+1):
        num1.append(i)
    count=len(list4)
    for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
    str1='0 0'
    for i in range(n):
        if num1[i]!=int(list4[i]):
            str1=list4[i]+' '+str(num1[i])
            break
    print(str1)
        