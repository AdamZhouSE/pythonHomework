T = int(input())
while T > 0:
    T -= 1
    A_length, B_length, num = input().split(' ')
    A_nums = input().split(' ')
    B_nums = input().split(' ')
    # A_length = int(A_length)
    # B_length = int(B_length)
    num = int(num)
    A = [int(A_nums[i]) for i in range(len(A_nums))]
    B = [int(B_nums[i]) for i in range(len(B_nums))]
    isExi = False
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if A[i] + B[j] == num:
                isExi = True
                print(str(A[i]) + ' ' + str(B[j]))
    if not isExi:
        print('-1')