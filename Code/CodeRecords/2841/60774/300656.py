def myIter(arr,mode):
    if(len(arr) == 1):
        return arr[0]
    elif(mode == 1):
        k = len(arr)
        temp = []
        for i in range(0,k,2):
            temp.append(arr[i] | arr[i + 1])
        return myIter(temp,2)
    elif(mode == 2):
        k = len(arr)
        temp = []
        for i in range(0,k,2):
            temp.append(arr[i] ^ arr[i + 1])
        return myIter(temp,1)

s = input().split(' ')
n = int(s[0])
m = int(s[1])
arr = list(map(int,input().split(' ')))
for t in range(0,m):
    q = input().split(' ')
    arr[int(q[0]) - 1] = int(q[1])
    value = myIter(arr,1)
    print(value)