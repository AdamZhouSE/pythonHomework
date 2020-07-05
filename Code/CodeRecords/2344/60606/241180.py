test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    d = int(input())
    part1 = array[0:d]
    part2 = array[d:]
    result = part2+part1
    for j in result:
        print(j,end=" ")
    print()
        