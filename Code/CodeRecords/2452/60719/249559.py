lines = int(input())
matrix = []
for i in range(lines):
    matrix.extend(input().split(","))
need = int(input())
start = 0
end = len(matrix)-1
mid = end//2
find = False
while int(matrix[mid]) != need and start <= end and int(matrix[start]) <= need <= int(matrix[end]):
    if int(matrix[mid]) < need:
        if mid == end:
            break
        if need < int(matrix[mid+1]):
            break
        start = mid
        mid = (start+end)//2
    else:
        if mid == start:
            break
        if need > int(matrix[mid-1]):
            break
        end = mid
        mid = end//2
if int(matrix[mid]) == need:
    print(True)
else:
    print(False)