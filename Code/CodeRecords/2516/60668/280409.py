if __name__ =='__main__':
    intervals = []
    for _ in range(int(input())):
        co = [int(i) for i in input().split(',')]
        intervals.append(co)
    size = len(intervals)
    indexes = [i for i in range(size)]
    indexes.sort(key=lambda i: intervals[i][0])


    def firstGreater(target: int) -> int:
        if target > intervals[indexes[-1]][0]:
            return -1

        l, r = 0, size - 1
        while l < r:
            mid = (l + r) >> 1
            if intervals[indexes[mid]][0] < target:
                l = mid + 1
            else:
                r = mid
        return indexes[l]
    print( [firstGreater(intervals[i][1]) for i in range(size)])