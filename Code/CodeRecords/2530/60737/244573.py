def my_sort(s, t):
    ans = ''
    used = []
    for i in range(len(s)):
        for j in range(len(t)):
            if t[j] == s[i]:
                ans += t[j]
                used.append(j)
    for k in range(len(t)):
        able = True
        for index in used:
            if k == index:
                able = False
                break
        if able:
            ans += t[k]
    return ans


if __name__ == "__main__":
    s = list(input())
    t = list(input())
    print(my_sort(s, t))
