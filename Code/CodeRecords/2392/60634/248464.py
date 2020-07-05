def find(P,size,arr):
    i = 0
    while i < size-1:
        j = i + 1
        while j < size:
            if int(arr[i])*int(arr[j]) == P:
                return "Yes"
            j += 1
        i += 1
    return "No"

pro =int(input())
for p in range(pro):
    temp = input().split(" ")
    size = int(temp[0])
    P = int(temp[1])
    arr = input().split(" ")
    
    print(find(P,size,arr))