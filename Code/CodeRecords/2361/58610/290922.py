import math

def num_square_perms(arr) -> int:
    res = [0]
    state = []
    s = set()

    def is_square(square_num):
        if int(math.sqrt(square_num)) ** 2 == square_num:
            return True
        return False

    def back(state, A):
        if tuple(state) in s:
            return
        s.add(tuple(state))
        if len(A) == 0:
            res[0] += 1
            if tuple(state[::-1]) not in s:
                s.add(tuple(state[-2:-1:-1]))
            return
        for i in range(len(A)):
            if len(state) == 0 or is_square(state[-1] + A[i]):
                back(state + [A[i]], A[:i] + A[i + 1:])

    back(state, arr)
    return res[0]

print(num_square_perms(list(map(int, input().split(',')))))