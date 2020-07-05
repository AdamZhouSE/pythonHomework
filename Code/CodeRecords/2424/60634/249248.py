test = int(input())
for t in range(test):
    size = int(input())
    arr = input().split(" ")

    if size%2 == 0:
        print(0)
    else:
        cont = True
        i = 0
        while cont and i <= (size-1)/2:
            j = 1
            while j <= len(arr):
                if j == len(arr):
                    print(arr[0])
                    cont = False
                    break
                if int(arr[j])==int(arr[0]):
                    arr.remove(arr[0])
                    arr.remove(arr[j-1])
                    break
                j += 1
            i += 1
