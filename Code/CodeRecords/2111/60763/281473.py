def nthUglyNumber(n):
    if n == 0:
        return 0
    arr = [0]*n
    arr[0]=1
    count,index2,index3,index5 = 1,0,0,0
    while count<n:
        # print(min(arr[index2]*2,arr[index3]*3,arr[index5]*5))
        arr[count] = min(arr[index2]*2,arr[index3]*3,arr[index5]*5)
        while arr[index2]*2<= arr[count]:
            index2+=1
        while arr[index3]*3<= arr[count]:
            index3+=1
        while arr[index5]*5<= arr[count]:
            index5+=1
        count+=1
    return arr[n-1]
n = int(input())
print(nthUglyNumber(n))