# 3
inp = input()
ID = list(inp)
n = len(ID) + 1
big_l = []
def permutations(arr, position, end):
    if position == end:
        ok = True
        for i in range(len(arr)):
            if i>0:
                if (ID[i-1] == 'I' and arr[i] < arr[i-1]) or (ID[i-1] == 'D' and arr[i] > arr[i-1]):
                    ok = False
                    break
        if ok:
            print(arr)
            import sys
            sys.exit(0)
            
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
arr = list(range(n))
permutations(arr, 0, len(arr))