def find_kth_element(array, kth):
    array.sort()
    return array[kth-1]


inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
arr = [int(x) for x in input().strip().split(" ")]
for i in range(m):
    inp = input().split(" ")
    if inp[0] == 'Q':
        l, r, k = int(inp[1]), int(inp[2]), int(inp[3])
        print(find_kth_element(arr[l-1:r], k))
    else:
        index, change = int(inp[1])-1, int(inp[2])
        arr[index] = change
