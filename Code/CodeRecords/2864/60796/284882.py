def bubble():
    for i in range(len(numbers)-1):
        j=0
        while j<len(numbers)-i-1:
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
                time[j],time[j+1]=time[j+1],time[j]
            j=j+1


N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
numbers=[]
r=0
time=[]
for i in range(N):
    now=ls[i]
    if not numbers.__contains__(now):
        numbers.append(now)
        time.append(1)
    else:
        ind=numbers.index(now)
        time[ind]=time[ind]+1
bubble()
i=0
while i<len(numbers):
    now=numbers[i]
    before=now-1
    after=now+1
    n_now=now*time[i]
    n_before=0
    n_after=0
    containbefore=False
    containafter=False
    if numbers.__contains__(before):
        containbefore=True
        n_before=before*time[numbers.index(before)]
    if numbers.__contains__(after):
        containafter=True
        n_after=after*time[numbers.index(after)]
    if n_after+n_before<n_now:
        #选择删除now、before、after
        del numbers[i]
        del time[i]
        if containbefore:
            del time[numbers.index(before)]
            numbers.remove(before)
        if containafter:
            del time[numbers.index(after)]
            numbers.remove(after)
        r=r+n_now
        i=i-1
    i=i+1

result=0
for i in range(len(time)):
    result=result+numbers[i]*time[i]
result=result+r
print(result)