tomato_slices = int(input())
cheese_slices = int(input())


def hamStrategy(tom, chs):
    if tom % 2 != 0 or tom < chs * 2 or chs * 4 < tom:
        return []
    else:
        ans = [tom // 2 - chs, chs * 2 - tom // 2]
        return ans


print(hamStrategy(tomato_slices, cheese_slices))
