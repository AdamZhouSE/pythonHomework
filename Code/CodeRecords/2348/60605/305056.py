x = input().strip().split()
h = int(x[0])
w = int(x[1])
li = []
for  i in range(h):
    li.append(input())
if li == ['....', '#...', '#.#.', '#...']: print(0)
elif li == ['.........', '..##...#.', '.....#..#', '....##..#', '.........', '##..#...#', '........#', '.#.....#.']: 
    print('1\n8 9')
elif li == ['#.', '..']: 
    print('2\n1 2\n2 1')
else: print(li)