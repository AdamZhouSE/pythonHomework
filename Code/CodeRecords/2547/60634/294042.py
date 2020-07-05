test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split(' ')
    k = int(input())
    defir = {"#"}
    count = 0
    i = 0
    while i < len(arr)-1:
        j = i + 1
        while j < len(arr):
            a = int(arr[i])
            b = int(arr[j])
            if a < b:
                a = a^b
                b = a^b
                a = a^b
            if a-b == k and str(a)+"#"+str(b) not in defir:
                count += 1
                defir.add(str(a)+"#"+str(b))
            j += 1
        i += 1
        
    print(count)


































