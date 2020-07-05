T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    A_nums = input().split(' ')
    B_nums = input().split(' ')
    A = [int(A_nums[i]) for i in range(len(A_nums))]
    B = [int(B_nums[i]) for i in range(len(B_nums))]
    isEq = True
    A_lst = list(A)
    B_lst = list(B)
    A_lst.sort()
    B_lst.sort()
    if A_lst == B_lst:
        print(1)
    else:
        print(0)
