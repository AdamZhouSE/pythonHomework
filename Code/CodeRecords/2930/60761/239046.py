n=int(input(""))
numlist=list(map(int,input("").split(" ")))
peak=0
for i in range(1,n-1):
    if numlist[i-1]<numlist[i] and numlist[i]>numlist[i+1]:
        peak+=1
    if numlist[i-1]>numlist[i] and numlist[i]<numlist[i+1]:
        peak+=1
print(peak)