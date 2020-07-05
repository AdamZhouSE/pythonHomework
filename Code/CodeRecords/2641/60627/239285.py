# 13
a = input()
b = input()
ok = False
def permutations(arr, position, end):
    if position == end:
        s = ''.join(arr)
        if b.find(s) != -1:
            ok = True
            
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
arr = list(a)
permutations(arr, 0, len(arr))

print(ok)