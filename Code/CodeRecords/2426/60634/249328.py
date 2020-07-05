test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split(" ")
    
    ability = int(arr[0])*int(arr[1])*int(arr[2])
    i = 0
    while i < n-2:
        j = i+1
        while j < n-1:
            k = j+1
            while k < n:
                temp = int(arr[i])*int(arr[j])*int(arr[k])
                if temp>ability:
                    ability = temp
                k += 1
            j += 1
        i += 1
    print(ability)