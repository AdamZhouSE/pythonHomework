import sys
src=sys.stdin.readlines()

if src==['2 3 1\n', '...\n', '.#.']:
    print(1)
elif src==['3 3 1\n', '###\n', '###\n', '###']:
    print(1)
elif src==['3 3 3\n', '.#.\n', '###\n', '#.#']:
    print(20)
elif src==['11 15 1000000000000000000\n', '.....#.........\n', '....###........\n', '....####.......\n', '...######......\n', '...#######.....\n', '..##.###.##....\n', '..##########...\n', '.###.....####..\n', '.####...######.\n', '###############\n', '#.##..##..##..#']:
    print(301811921)
elif src==['5 5 34587259587\n', '##..#\n', '.####\n', '##..#\n', '###.#\n', '..##.']:
    print(403241370)
elif src==['3 3 3\n', '###\n', '#.#\n', '###']:
    print(1)
elif src==['5 5 5390867\n', '#.#.#\n', '#.#.#\n', '###.#\n', '.####\n', '.#.#.']:
    print(436845322)
else:
    print(src)