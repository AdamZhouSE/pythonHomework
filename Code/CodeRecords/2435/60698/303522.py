def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    words = []
    for _ in range(0, n):
        word = input()
        words.append(word)
    for _ in range(0, m):
        seg = input().split()
        seg = list(map(int, seg))
        begin = seg[0] - 1
        end = seg[1] - 1
        words_seg = words[begin:end + 1]
        words_seg.sort()
        words_seg.reverse()
        print(words_seg[0])
        

test()
