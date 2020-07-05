def h12():
    n = int(input())
    arr = list(map(int,input().split()))
    # n = 5
    # arr = [1,1,1,1,1]
    i = 0
    while(i<len(arr)):
        while(arr[i]==0):
            arr.remove(arr[i])
            if(len(arr)==0):
                break
        j = i+1
        while(j<len(arr)):
            if (arr[i] == arr[j]):
                arr.remove(arr[j])
                j -= 1
            j += 1
        i += 1
    print(len(arr))

if __name__ == '__main__':
    h12()