n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
for _ in range(m):
    ope = input().split()
    if ope[0] == 'Q':
        temp_arr = sorted(arr[int(ope[1])-1:int(ope[2])])
        print(temp_arr[int(ope[3]) - 1])
    elif ope[0] == 'C':
        arr[int(ope[1]) - 1] = int(ope[2])