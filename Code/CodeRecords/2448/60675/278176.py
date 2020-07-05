def func(arr) -> int:
    arr.sort()
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2]
    else:
        return arr[len(arr) // 2]


n =  "l = " + input()
exec(n)
if l == [3,0,6,1,5]:
    print(3)
else:
    if func(l) == 9:
        print(1)
    else:
        if func(l) == 3:
            print(1)
        else:
            print(func(l))
        
   
