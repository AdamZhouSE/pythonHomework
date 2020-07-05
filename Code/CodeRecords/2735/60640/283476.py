def find_kth_element(array, kth):
    array.sort()
    return array[kth-1]


inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
arr = [int(x) for x in input().strip().split(" ")]
for i in range(m):
    inp = input().split(" ")
    l, r, k = int(inp[0]), int(inp[1]), int(inp[2])
    print(find_kth_element(arr[l-1:r], k))
