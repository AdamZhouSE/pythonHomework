def characterReplacement(s: str, k: int) -> int:
    if str == "": return 0
    d = [0] * 26
    left = 0
    right = 0
    re = 0
    d[ord(s[right]) - ord("A")] += 1
    while right < len(s) - 1:
        most = max((d), default=0)
        if right - left + 1 <= most + k:
            if re < right - left + 1:
                re = right - left + 1
            right += 1
            d[ord(s[right]) - ord("A")] += 1
        else:
            d[ord(s[left]) - ord("A")] -= 1
            left += 1
    most = max((d), default=0)
    if right - left + 1 <= most + k and re < right - left + 1:
        re = right - left + 1
    return re

if __name__ == "__main__":
    s = input()
    k = int(input())
    re = characterReplacement(s, k)
    print(re)