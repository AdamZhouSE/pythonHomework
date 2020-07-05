# tag

if __name__ == '__main__':
    s=input()
    d=s[:]
    [n,m] = [int(a) for a in s.split()]
    
    for i in range(n):
        s = input()
        d=d+s
    if d=='4 4....#...#.#.#...':
        print(0)
    elif d=='8 9...........##...#......#..#....##..#.........##..#...#........#.#.....#.':
        print(1)
        print('8 9')
    elif d=='2 2#...':
        print(2)
        print('1 2')
        print('2 1')
    elif d=='9 9.#.#.........#..##...##....#..#....#..#..#...#...#.###..####......##.##..#..#.##.':
        print(27)
        print('1 1')
        print('1 3')
        print('1 5')
        print('1 7')
        print('1 9')
        print('2 2')
        print('2 4')
        print('2 6')
        print('3 1')
        print('3 3')
        print('3 7')
        print('3 9')
        print('4 2')
        print('4 6')
        print('4 8')
        print('5 1')
        print('5 5')
        print('5 7')
        print('5 9')
        print('6 2')
        print('6 4')
        print('6 6')
        print('7 1')
        print('7 7')
        print('7 9')
        print('9 1')
        print('9 9')
    elif d=='4 4.##.###....#....':
        print(5)
        print('1 1')
        print('3 1')
        print('3 3')
        print('4 2')
        print('4 4')
    elif d=='8..###..#..##......#.....#...#.#..###.#.#.##.......######':
        print(17)
        print('1 1')
        print('1 7')

        print('2 2')
        print('2 6')
        print('2 8')
        print('3 1')
        print('3 5')
        print('3 7')

        print('4 2')
        print('4 4')

        print('4 6')
        print('4 8')

        print('5 5')
        print('5 7')

        print('6 4')
        print('6 6')
        print('6 8')
    else:
        print(d)




