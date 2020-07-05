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
        print(sequence)
        print(length)
        print(len(sequence)
     print(min(upCounts, downCounts))

if __name__=='__main__':
    construct_sequence()