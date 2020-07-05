
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def union(array, start, end):
    flag = False
    for i in array[start]:
        for j in range(len(array[end])):
            if gcd(i, array[end][j]) > 1:
                array[start].extend(array[end])
                array.pop(end)
                flag = True
                break
        if flag:
            break
    return array


temp = input()
A = eval('[' + temp + ']')
A.sort()
A = A[::-1]
for i in range(len(A)):
    A[i] = [A[i]]
start = 0
end = 1
while start < len(A):
    while start < len(A) and end < len(A):
        temp = union(A[:], start, end)
        if len(temp) == len(A):
            end = end + 1
            if start == end:
                end = end + 1
        A = temp
    start = start + 1
    end = 0
length = 0
for i in range(len(A)):
    length = max(length, len(A[i]))
print(length)