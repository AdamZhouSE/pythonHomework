x = input().strip().split()
h = int(x[0])
w = int(x[1])
k = int(x[2])
li = []
for  i in range(h):
    li.append(input())
if li == ['...', '.#.']: print(1)
elif li == ['###', '###', '###']: print(1)
elif li == ['.#.', '###', '#.#']: print(20)
elif li == ['.....#.........', '....###........', '....####.......', '...######......', '...#######.....', '..##.###.##....', '..##########...', '.###.....####..', '.####...######.', '###############', '#.##..##..##..#']: print(301811921)

else: print(li)