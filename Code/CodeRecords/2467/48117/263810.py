questNum = int(input())

for i1 in range(questNum):
    mnk = input().split(' ')
    m = int(mnk[0])
    n = int(mnk[1])
    k = int(mnk[2])
    A = input().split(' ')
    B = input().split(' ')

    count = 2
    i = 0
    j = 0
    while i <= max(len(A), len(B)) and j <= max(len(A), len(B)):
        if count == k:
            print(max(A[i], B[j]))
            break
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                i += 1
            else:
                j += 1
            count += 1
        else:
            if i >= len(A):
                j += k - count
                count = k
            else:
                i += k - count
                count = k