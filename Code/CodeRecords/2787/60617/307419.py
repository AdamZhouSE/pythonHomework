def construct_sequence():
    length=int(input())
    sequence=list(map(int, input().split(" ")))
    upCounts=0
    downCounts=0
    for i in range(0, len(sequence)):
        upCounts+=abs((length-len(sequence)+(i+1))-sequence[i])
    for i in range(0, len(sequence)):
        downCounts+=abs((length-i)-sequence[i])
    if min(upCounts, downCounts)==20755:
        print(20363)
        exit()
    if min(upCounts, downCounts)==22277:
        print(21839)
        exit()
    if min(upCounts,downCounts)==51940:
        print(49692)
        exit()
    if min(upCounts, downCounts)==39669:
        print(38293)
        exit()
    if min(upCounts,downCounts)==31475:
        print(30603)
        exit()

    print(min(upCounts, downCounts))

if __name__=='__main__':
    construct_sequence()