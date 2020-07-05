def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
def judge(arr,brr):
    d1=abs(arr[0]-brr[0])+abs(arr[1]-brr[1])
    d2=((arr[0]-brr[0])**2+(arr[1]-brr[1])**2)**0.5
    if float(d1)==d2:
        return 1
    else:
        return 0
n=int(input())
points=[]
for i in range(n):
    points.append(nums(input()))
answer=0
for i in range(n-1):
    for j in range(i+1,n):
        if judge(points[i],points[j])==1:
            answer+=1
        else:
            continue
if answer==1:
    print(points)
print(answer)