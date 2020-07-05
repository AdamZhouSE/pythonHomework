def panSort():
    arr=list(eval(input()))
    res=[]
    for i in range(0, len(arr)-1):
        idx=arr.index(max(arr[0:len(arr)-i]))
        res.append(idx+1)
        reverse(arr, idx)
        res.append(len(arr)-i-1)
        reverse(arr, len(arr)-i-1)
    print(res)

def reverse(arr, index):
    temp=arr[:index+1].copy()
    temp=temp[::-1]
    for i in range(0, index+1):
        arr[i]=temp[i]
if __name__=='__main__':
    panSort()
