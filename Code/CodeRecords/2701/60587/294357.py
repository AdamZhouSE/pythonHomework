inp = input()
tmp = inp[2:len(inp) - 2]
nums = tmp.split('],[')
n = len(nums)
lst = []
moves = []
for num in nums:
    lst.append(int(num[0]))
    lst.append(int(num[2]))
    moves.append(lst)

A = [0] * 8
B = [0] * 8
l = len(moves)
for n in range(l):
    if n % 2:
        B[moves[n][0]] += 1
        B[moves[n][1] + 3] += 1
        if moves[n][0] == moves[n][1]:
            B[6] += 1
        if moves[n][0] + moves[n][1] == 2:
            B[7] += 1
    else:
        A[moves[n][0]] += 1
        A[moves[n][1] + 3] += 1
        if moves[n][0] == moves[n][1]:
            A[6] += 1
        if moves[n][0] + moves[n][1] == 2:
            A[7] += 1

if max(A) == 3:
    print('A')
elif max(B) == 3:
    print('B')
elif l == 9:
    print('Draw')
else:
    print('Pending')
