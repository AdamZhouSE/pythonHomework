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
selected=[]
for i in range(N):
    now=ls[i]
    if not numbers.__contains__(now):
        numbers.append(now)
        time.append(1)
    else:
        ind=numbers.index(now)
        time[ind]=time[ind]+1
    selected.append(False)
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
        #选择now,不选before、after
        selected[i]=True
        if containbefore:
            selected[numbers.index(before)]=False
        if containafter:
            selected[numbers.index(after)]=False
    else:
        #选择before、after，不选now
        selected[i] = False
        if containbefore:
            selected[numbers.index(before)] = True
        if containafter:
            selected[numbers.index(after)] = True
    i=i+1
result=0
for i in range(len(time)):
    if selected[i]:
        result=result+numbers[i]*time[i]

print(result)