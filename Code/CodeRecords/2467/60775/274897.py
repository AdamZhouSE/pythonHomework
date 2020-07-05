def print_list(nums:list):
    #打印数组
    for i in range(len(nums)):
        print(str(nums[i]) + ' ',end='')
    print()


def do(A:list, B:list, k):
    result = []
    idxA = 0
    idxB = 0
    while True:
        if idxA == len(A):
            result.extend(B[idxB:])
            return result[k-1]
        elif idxB == len(B):
            result.extend(A[idxA:])
            return result[k-1]
        else:
            if A[idxA] < B[idxB]:
                tmp = A[idxA]
                result.append(tmp)
                idxA += 1
            else:
                tmp = B[idxB]
                result.append(tmp)
                idxB += 1



T = int(input())
for t in range(T):
    input1 = input().split(' ')
    sizeA = int(input1[0])
    sizeB = int(input1[1])
    k = int(input1[2])
    A = [int(x) for x in input().split(' ')]
    B = [int(x) for x in input().split(' ')]
    print(do(A,B,k))







