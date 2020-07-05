n, size = list(map(int, input().split(' ')))
songs = [list(map(int, input().split(' '))) for _ in range(n)]
diff = sorted([x[0] - x[1] for x in songs], reverse=True)

def solution():
    count = 0
    now_size = sum([x[0] for x in songs])
    for i in diff:
        if now_size <= size:
            return count
        else:
            now_size -= i
            count += 1
    return count if now_size <= size else -1

print(solution())
