length=int(input())
sushi=[int(x) for x in input().split()]
key=sushi[0]
count=1
statistics=[]
for i in range(1,length):
    if sushi[i]==key:
        count+=1
    else:
        statistics.append(count)
        count=1
        key=sushi[i]
statistics.append(count)
maximum=0
for i in range(1,len(statistics)):
    maximum=max(maximum,min(statistics[i],statistics[i-1])*2)
print(maximum)