li=input().split()
c=int(li[0])
n=int(li[1])
arr=[]
ma=0
for i in range(n):
    li=input().split()
    arr.append([int(li[0]),int(li[1])])
    if max(int(li[0]),int(li[1]))>ma:
        ma=max(int(li[0]),int(li[1]))
mins=ma+1
for i in range(ma):
    for j in range(i,ma+1):
        count=0
        for k in range(len(arr)):
            if arr[k][0]>=i and arr[k][0]<=j:
                if arr[k][1]>=i and arr[k][1]<=j:
                    count+=1
        if count>=c:
            if j-i+1<mins:
                mins=j-i+1
print(mins)
        

    