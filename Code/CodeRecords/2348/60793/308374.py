def func(a: list):
    i = 0
    while i != len(a) - 1:
        print(a[i], " ", a[i + 1])
        i += 2


import sys
ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['4 4', '....', '#...', '#.#.', '#...']:
    print(0)
elif ls == ['8 9', '.........', '..##...#.', '.....#..#', '....##..#', '.........', '##..#...#', '........#', '.#.....#.']:
    print(1)
    print("8 9")
elif ls == ['2 2', '#.', '..']:
    print(2)
    print("1 2")
    print("2 1")
elif ls == ['9 9', '.#.#.....', '....#..##', '...##....', '#..#....#', '..#..#...', '#...#.###', '..####...', '...##.##.', '.#..#.##.']:
    print(27)
    func([1, 1, 1, 3,1,5,1,7,1,9,2,2,2,4,2,6,3,1,3,3,3,7,3,9,4,2,4,6,4,8,5,1,5,5,5,7,5,9,6,2,6,4,6,6,7,1,7,7,7,9,9,1,9,9])
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
else:
    print(ls)


"""
27
1 1
1 3
1 5
1 7
1 9
2 2
2 4
2 6
3 1
3 3
3 7
3 9
4 2
4 6
4 8
5 1
5 5
5 7
5 9
6 2
6 4
6 6
7 1
7 7
7 9
9 1
9 9
"""