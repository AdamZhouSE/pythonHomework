def search(matrix, target):
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if target < int(matrix[0][0]) or target > int(matrix[m-1][n-1]):
            return False
        left = 0
        right = m - 1
        while left <= right:
            mid = (left + right) // 2
            if int(matrix[mid][0]) == target:
                return True
            elif target > int(matrix[mid][0]):
                left = mid + 1
            else:
                right = mid - 1
        tmp = right
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if int(matrix[tmp][mid]) == target:
                return True
            elif target > int(matrix[tmp][mid]):
                left = mid + 1
            else:
                right = mid - 1
        return False
n=int(input())
matrix=[]
for i in range(n):
    t=list(input())
    matrix.append(t)
target=int(input())
answer=search(matrix,n)
print(answer)