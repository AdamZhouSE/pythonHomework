def swap(x, y, arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def sort(i,arr):
    while i > 0:
        if arr[i][1] > arr[i-1][1]:
            swap(i,i-1,arr)
        elif arr[i][1] == arr[i-1][1]:
            if arr[i][0] > arr[i-1][0]:
                swap(i,i-1,arr)
            else:
                break
        else:
            break
        i -= 1

def filter(vfl,maxPri,maxDist,arr):
    i = 0
    result = []
    while i < len(arr):
        if (vfl==1)and(arr[i][2] == vfl)and(arr[i][3]<=maxPri)and(arr[i][4]<=maxDist):
            sort(i,arr)
        elif (vfl==0)and(arr[i][3]<=maxPri)and(arr[i][4]<=maxDist):
            sort(i,arr)
        else:
            arr.remove(arr[i])
            i -= 1
        i += 1
    for x in arr:
        result.append(x[0])
    return result

inform = eval(input())
VFL = int(input())
maxPri = int(input())
maxDist = int(input())


print(filter(VFL,maxPri,maxDist,inform))









