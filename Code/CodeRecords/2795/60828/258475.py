def h17():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    i = 1
    while(i<len(arr)):
        for j in range(i-1,-1,-1):
            if(arr[j]==arr[i]):
                arr.remove(arr[j])
                i -= 1
        i += 1
    res = -1
    if(len(arr)==1):
        res = 0
    elif(len(arr)==2):
        if((arr[0]+arr[1])%2==0):
            res = (arr[1]-arr[0])/2
        else:
            res = arr[1]-arr[0]
    elif(len(arr)==3 and arr[1]==(arr[0]+arr[2])/2):
        res = arr[1]-arr[0]
    print(int(res))

if __name__ == '__main__':
    h17()