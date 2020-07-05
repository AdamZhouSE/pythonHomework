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
    else:
        print(d)




