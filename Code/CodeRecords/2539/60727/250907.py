a=input()
le = len(a)
a= a[1:le-1]
li = a.split(',')
li = list(map(int,li))
ll=sorted(li)
start = 0
startFlag=0
end = 0
endFlag=0
for i in range(0,len(ll)):
    if startFlag==0:
        if ll[i]!=li[i]:
            start=i
            starFlag=1
    if startFlag==1 and i!=start:
        if li[i]!=ll[i]:
            endFlag+=1
            end = i
if abs(end-start)==1:
    print (2)
else:
    
    print(abs(end-start))

