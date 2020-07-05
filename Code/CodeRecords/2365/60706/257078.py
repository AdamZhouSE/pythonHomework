t=int(input())
for i in range(t):
    n=int(input())
    list4=input().split()
    num=[]
    for s in range(len(list4)):
        num.append(int(list4[s]))
    n=5
    for i in range(len(list4)):
        while len(list4[i])<n:
            list4[i]=list4[i]+'0'
    count=len(list4)
    for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) <int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
                num[i],num[j]=num[j],num[i]
            elif int(list4[i])==int(list4[j]):
                if num[i]>num[j]:
                    num[i],num[j]=num[j],num[i]
    str1=''
    for i in range(len(num)):
        str1=str1+str(num[i])
    print(str1)
    