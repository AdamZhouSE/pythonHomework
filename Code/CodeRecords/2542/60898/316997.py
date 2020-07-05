arr=sorted(eval(input()))
cnt=1
maxcnt=1
for i in range(1,len(arr)):
    if arr[i]-arr[i-1]==1:
        cnt+=1
    else:
        if cnt>maxcnt:
            maxcnt=cnt
        cnt=1
print(maxcnt)