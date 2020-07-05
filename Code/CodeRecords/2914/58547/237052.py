def func():
    n = int(input())
    arr_a = [int(x) for x in input().split(" ")]
    arr_b = [int(x) for x in input().split(" ")]
    
    arr_c = []
    i = 0
    while i < n:
        arr_c.append(arr_a[i] - arr_b[i])
        i += 1
        
    if len(set(arr_c)) <= 2:
        print("YES")
    else:
        print("NO")
        

func()
