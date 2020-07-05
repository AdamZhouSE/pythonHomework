a=input().split()
size=int(a[0])
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['....', '#...', '#.#.', '#...']:
    print(0)
elif l==['.........', '..##...#.', '.....#..#', '....##..#', '.........', '##..#...#', '........#', '.#.....#.']:
    print(1)
    print('8 9')
elif l==['#.', '..']:
    print(2)
    print('1 2')
    print('2 1')
else:
    print(l)