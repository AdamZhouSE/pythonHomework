"""给你一个 n 行 m 列的白色矩阵，这个白色矩阵中存在一个边长为奇数的黑色子矩阵，请你求出这个黑色子矩阵的中心位置的坐标。"""

n_and_m = input().split()
n = int(n_and_m[0])
m = int(n_and_m[1])

found_first_B = False
is_B_in_line = False
for i in range(0, n):
    if found_first_B and ((i - pos_of_top_left_B[0]) % 2 != 0):
        a = input()  # 这个输入用不到，只是为了消耗掉一行
        if i == (n - 1):
            print(str(pos_of_top_left_B[0] + 1) + " " + str(pos_of_top_left_B[1] + 1))
            break

    else:
        line = input()
        index_in_line = 0

        for c in line:

            if c == "B":
                is_B_in_line = True

                if not found_first_B:
                    pos_of_top_left_B = (i, index_in_line)
                    found_first_B = True

                pos_of_B = (i, index_in_line)
                break

            index_in_line += 1

        else:
            if is_B_in_line:
                length_of_side = pos_of_B[0] - pos_of_top_left_B[0]
                result = (
                    pos_of_top_left_B[0] + length_of_side // 2 + 1, pos_of_top_left_B[1] + length_of_side // 2 + 1)

                print(str(result[0]) + " " + str(result[1]))
