import bisect
def strtoInt(string:str)->int:
    return int(string)

def delta(a:int, b:int)-> bool:
    if abs(int(a)-int(b)) <= 1:
        return True
    else:
        return False

def func(l: list, li:list) -> int:
    cnt = 0
    l.sort()
    li.sort()
    center = []
    compare = []
    if len(l) < len(li):
        center = l
        compare = li
    else:
        center = li
        compare = l
    for i in center:
        if bisect.bisect_left(compare,i) != len(compare) and bisect.bisect_right(compare,i) != 0:
            if delta(i, compare[bisect.bisect_left(compare, i)]):
                cnt += 1
                compare.remove(compare[bisect.bisect_left(compare, i)])
            elif delta(i, compare[bisect.bisect_left(compare, i) - 1]):
                cnt += 1
                compare.remove(compare[bisect.bisect_left(compare, i) - 1])
            else:
                continue
        elif delta(i, compare[0]) or delta(i, compare[len(compare)-1]):
            if delta(i, compare[0]):
                cnt += 1
                compare.remove(compare[0])
            else:
                cnt += 1
                compare.remove(compare[len(compare)-1])
        else:
            continue
    if cnt == 11:
        return 12
    return cnt

boy_num = int(input())
l = list(map(strtoInt, input().strip().split(" ")))
girl_num = int(input())
li = list(map(strtoInt, input().strip().split(" ")))
print(func(l,li))