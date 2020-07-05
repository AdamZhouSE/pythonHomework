def longest_subUparr():
    arr=eval("["+input()+"]")
    res=[2**16,0]
    for i in range(0,len(arr)-1):
        if arr[i]>res[0]:
            continue
        count=1
        temp=arr[i]
        for j in range(i, len(arr)):
            if temp<arr[j]:
                temp=arr[j]
                count+=1
        if count>res[1]:
            res[0]=arr[i]
            res[1]=count
    print(res[1])

if __name__=='__main__':
    longest_subUparr()