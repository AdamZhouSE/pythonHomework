t=int(input())
for i in range(0,t):
    arr=list(input())
    re=[]
    def cal(index,s):
        if index==len(arr)-1:
            re.append(s)
        else:
            for i in range(index+1,len(arr)):
                if arr[i]>s[-1]:
                    cal(i,s+arr[i])
                if i==len(arr)-1 and arr[i]<=s[-1]:
                    cal(i,s)
    for i in range(0,len(arr)):
        cal(i,arr[i])
    length=0
    for i in range(0,len(re)):
        if len(re[i])>length:
            length=len(re[i])
    print(length)