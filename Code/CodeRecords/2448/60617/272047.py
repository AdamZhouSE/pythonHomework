def H_exponent():
    arr=list(eval(input()))
    arr.sort()
    H=0
    for i in range(0, len(arr)):
        if arr[i]>len(arr):
            break
        else:
            temp=arr[i]
            times=1
            for j in range(i+1, len(arr)):
                if arr[j]>=temp:
                    times+=1
            if times>=temp:
                H=temp
    print(H)
    
if __name__=='__main__':
    H_exponent()