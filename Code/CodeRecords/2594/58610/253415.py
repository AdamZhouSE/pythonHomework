def solution(s: str) -> int:
    word_index = dict()
    max_len = -1
    for index in range(len(s)):
        if word_index.get(s[index], -1) == -1:
            word_index[s[index]] = index
        max_len = max(index - word_index.get(s[index], len(s)) - 1, max_len)
    return max_len

for _ in range(eval(input())):
    print(solution(input().lower()))
