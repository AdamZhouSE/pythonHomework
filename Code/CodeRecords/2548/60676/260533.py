def longest_substring_with_k_elements(s, k):
    res = 0
    for i in range(len(s)):
        tmp = [s[i]]
        j = i + 1
        while j < len(s) and len(tmp) <= k:
            if s[j] not in tmp:
                if len(tmp) == k:
                    break
                else:
                    tmp.append(s[j])
            j += 1
        if j - i + 1 > res:
            res = j - i
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        k = int(input())
        result.append(longest_substring_with_k_elements(a, k))
    for i in range(len(result)):
        print(result[i])