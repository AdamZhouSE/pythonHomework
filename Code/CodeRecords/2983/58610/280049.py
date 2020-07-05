s_len = eval(input())
s_get = input()

def solve(s: list, length: int):
    count = 0
    have_single = False
    end = length - 1
    for i in range(0, end + 1):
        for j in range(end, i - 1, -1):
            if i == j:
                if length % 2 == 0 and have_single:
                    return "Impossible"
                else:
                    # 单数个元素，放到中间去
                    have_single = True
                    count += length // 2 - i
            elif s[i] == s[j]:
                for k in range(j, end):
                    s[k], s[k + 1] = s[k + 1], s[k]
                    count += 1
                end -= 1
                break
    return count

print(solve(list(s_get), s_len))