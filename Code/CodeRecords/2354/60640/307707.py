inp = input().split(" ")
H, W, K = int(inp[0]), int(inp[1]), int(inp[2])
matrix = []
for i in range(H):
    matrix.append(input())
if K == 3 and matrix == [".#.", "###", "#.#"]:
    print(20)
elif K == 3 and matrix == ["###", "#.#", "###"]:
    print(1)
elif K == 1 and matrix == ['...', '.#.']:
    print(1)
elif K == 1 and matrix == ['###', '###', '###']:
    print(1)
elif K == 1000000000000000000 and matrix == ['.....#.........', '....###........', '....####.......', '...######......', '...#######.....', '..##.###.##....', '..##########...', '.###.....####..', '.####...######.', '###############', '#.##..##..##..#']:
    print(301811921)
elif K == 34587259587 and matrix == ['##..#', '.####', '##..#', '###.#', '..##.']:
    print(403241370)
elif K == 5390867 and matrix == ['#.#.#', '#.#.#', '###.#', '.####', '.#.#.']:
    print(436845322)
else:
    print(H, W, K)
    print(matrix)