def odd_even():
    arr=eval(input())
    res=[]
    for i in range(0, len(arr)):
        if arr[i]%2==0:
            res.append(arr[i])
    loc=1
    for ele in arr:
        if ele%2!=0:
            res.append(ele)
    print(res)

if __name__=='__main__':
    odd_even()