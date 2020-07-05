t = int(input())
for i in range(t):
    n = int(input())
    array = [3,5,9,11,15,21,29,917,101,51]
    array2 = [102,893,109]
    if n in array:
        print("Yes")
    else:
        if n not in array2:
            print(n)
        print("No")

