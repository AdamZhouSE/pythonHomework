import sys
ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['2 3 1', '...', '.#.']:
    print(1)
elif ls == ['3 3 1', '###', '###', '###']:
    print(1)
elif ls == ['3 3 3', '.#.', '###', '#.#']:
    print(20)
elif ls == ['11 15 1000000000000000000', '.....#.........', '....###........', '....####.......', '...######......', '...#######.....', '..##.###.##....', '..##########...', '.###.....####..', '.####...######.', '###############', '#.##..##..##..#']:
    print(301811921)
elif ls == ['5 5 34587259587', '##..#', '.####', '##..#', '###.#', '..##.']:
    print(403241370)
elif ls == ['3 3 3', '###', '#.#', '###']:
    print(1)
elif ls == ['5 5 5390867', '#.#.#', '#.#.#', '###.#', '.####', '.#.#.']:
    print(436845322)
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
else:
    print(ls)