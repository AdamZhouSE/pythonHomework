arr=(eval(input()))
re=[]
now='JFK'
re.append(now)
n=len(arr)
for i in range(n):
    nn='ZZZ'
    ind=0
    for j in range(len(arr)):
        if arr[j][0]==now:
            if arr[j][1]<=nn:
                nn=arr[j][1]
                ind=j
    del arr[ind]
    now=nn
    re.append(now)
print(re)