def ordering(temp,start,end):
    if start>=end:
        if len(set(temp))==len(temp):res.append(temp)
    else:
        ordering(temp+arr[start],start+1,end)
        ordering(temp, start + 1, end)


arr=input()[2:-2].split('","')
res=[]
ordering("",0,len(arr))
maxLen=0
for i in res:
    maxLen=max(maxLen,len(i))
print(maxLen)