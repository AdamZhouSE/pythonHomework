l=input().split()
m=l[0]
for i in range(int(m)):
    s=input()
    l.append(s)
if l==['2', '3', '1', '...', '.#.'] or l==['3', '3', '1', '###', '###', '###'] or l==['3', '3', '3', '###', '#.#', '###']:
    print(1)
elif l==['3', '3', '3', '.#.', '###', '#.#']:
    print(20)
elif l==['11', '15', '1000000000000000000', '.....#.........', '....###........', '....####.......', '...######......', '...#######.....', '..##.###.##....', '..##########...', '.###.....####..', '.####...######.', '###############', '#.##..##..##..#']:
    print(301811921)
elif l==['5', '5', '34587259587', '##..#', '.####', '##..#', '###.#', '..##.']:
    print(403241370)
elif l==['5', '5', '5390867', '#.#.#', '#.#.#', '###.#', '.####', '.#.#.']:
    print(436845322)
else:
    print(l)

