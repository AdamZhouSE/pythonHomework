def findKth(matrix,k,start,end):
    nowMid = 0
    smallN = 0
    equalN = 1
    mid = int((start+end)/2)
    for row in matrix:
        for i in row:
            if i <= mid:
                smallN = smallN + 1
                if i > nowMid:
                    nowMid = i
                    equalN = 1
                elif i == nowMid:
                    equalN = equalN +1
            else:
                break
    if (smallN - equalN < k) and (smallN >= k):
        return nowMid
    elif smallN < k:
        return findKth(matrix,k,mid+1,end)
    else:
        return findKth(matrix,k,start,nowMid-1)
    
numOfInput = int(input())
matrix = []
for i in range(numOfInput):
    row = input().split(",")
    row = list(map(int,row))
    matrix.append(row)
k = int(input())
print(findKth(matrix,k,matrix[0][0],matrix[-1][-1]))