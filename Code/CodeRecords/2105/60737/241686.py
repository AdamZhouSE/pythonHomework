def total_area(locs):
    total = (locs[2] - locs[0]) * (locs[3] - locs[1]) + (locs[6] - locs[4]) * (locs[7] - locs[5])
    long = ((locs[2] + locs[6] - locs[0] - locs[4]) - abs(locs[4] - locs[0]) - abs(locs[6] - locs[2])) / 2
    height = ((locs[3] + locs[7] - locs[1] - locs[5]) - abs(locs[5] - locs[1]) - abs(locs[7] - locs[3])) / 2
    return int(total - long * height)


if __name__ == "__main__":
    s = [int(n) for n in input().split(', ')]
    print(total_area(s))
