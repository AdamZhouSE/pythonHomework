testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawArr=input().split(' ')
    arr=[]
    for item in rawArr:arr.append(int(item))
    ans=[]
    arr.sort();
    if(size<3): print('-1')
    else:
        doExist = False
        for j in range(0,size-2):
            for n in range(j+1,size-1):
                for m in range(n+1,size):
                    if(arr[j]+arr[n]==arr[m]):
                        ans.append([arr[j],arr[n],arr[m]])
        num=len(ans)
        if(num==0):print('-1')
        else :
            print(str(num))