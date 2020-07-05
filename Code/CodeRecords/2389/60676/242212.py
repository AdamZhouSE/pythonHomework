def wave_array(arr):
    for i in range(len(arr)//2):
        temp = arr[2*i]
        arr[2*i] = arr[2*i+1]
        arr[2*i+1] = temp


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    wave_array(array)
    result.append(array)
for i in range(len(result)):
    for j in range(len(result[i])-1):
        print(result[i][j], end=' ')
    print(result[i][len(result[i])-1])