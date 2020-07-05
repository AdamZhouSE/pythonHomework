
def has_next(index, count):
    for i in range(index+1, len(arr)):
        if arr[i] == arr[index] + difference:
            count += 1
            count = has_next(i, count)
            break
    return count


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    difference = int(input())
    counts = []
    for i in range(0, len(arr)):
        counts.append(has_next(i, 1))
    m = counts[0]
    for i in counts:
        if i > m:
            m = i
    print(m)
