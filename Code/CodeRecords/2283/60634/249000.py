test = int(input())
for t in range(test):
    size = int(input())
    arr = input().split(" ")
    
    result0 = []
    result1 = []
    result2 = []
    for ch in arr:
        if ch == '0':
            result0.append(0)
        elif ch == '1':
            result1.append(1)
        else:#if ch == '2':
            result2.append(2)
    arr = result0 + result1 + result2
    i = 0
    while i < size:
        print(arr[i],end = "")
        if i != size-1:
            print(end=" ")
        i += 1
    print()