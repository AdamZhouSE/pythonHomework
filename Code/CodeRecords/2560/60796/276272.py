def bubble(number,time):
    for i in range(len(time)-1):
        j=0
        while j<len(time)-i-1:
            if time[j]>time[j+1]:
                time[j],time[j+1]=time[j+1],time[j]
                number[j],number[j+1]=number[j+1],number[j]
            j=j+1
    return number,time


N=int(input())
result=[]
while N>0:
    n=int(input())
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    m=int(input())
    number=[]
    time=[]
    for i in range(len(ls)):
        if number.__contains__(ls[i]):
            ind=number.index(ls[i])
            time[ind]=time[ind]+1
        else:
            number.append(ls[i])
            time.append(1)
    s=bubble(number,time)
    number=s[0]
    time=s[1]

    while m>0:
        a=time[0]
        if m>=a:
            del time[0]
            m=m-a
        else:
            a=a-m
            m=0

    result.append(len(time))
    N=N-1

for i in range(len(result)):
    print(result[i])
