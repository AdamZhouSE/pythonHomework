#main-----
pro = int(input())
for p in range(pro):
    temp = input().split(' ')
    n = int(temp[0])
    s = int(temp[1])
    
    arr1 = arr2 = []
    count = 0
    
    for x in range(n):
        temp = input().split(' ')
        for y in range(n):
            arr1.append(int(temp[y]))
    
    for x in range(n):
        temp = input().split(' ')
        for y in range(n):
            curr = int(temp[y])
            for a in arr1:
                if curr + a == s:
                    count += 1
                    
    print(count)
            
    