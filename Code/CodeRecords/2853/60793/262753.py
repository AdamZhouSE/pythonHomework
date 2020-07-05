def odd_num(ls: list) -> int:
    result = 0
    for i in ls:
        if i % 2 != 0:
            result += 1
    return result


input()
cookies = list(map(int, input().split()))
if sum(cookies) % 2 == 0:
    print(odd_num(cookies))
else:
    print(len(cookies) - odd_num(cookies))