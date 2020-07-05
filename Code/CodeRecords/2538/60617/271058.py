def missingPos():
    arr=list(eval(input()))
    arr.sort()
    for i in range(arr[0], arr[-1]+1):
        if not i in arr:
            print(i)
            break
    if i==0:
        print(arr)
    
if __name__=='__main__':
    missingPos()
    