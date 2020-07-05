T = int(input())
# result = ''

for i in range(T):
    A_and_B = input().split()
    A = int(A_and_B[0])
    B = int(A_and_B[1])
    if (2 <= B) and (B <= A):
        print('1')
    else:
        print('0')
