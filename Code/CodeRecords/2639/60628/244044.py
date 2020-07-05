def findmaxlen(s,k):
    k = int(k)
    max_len = k
    start = 0
    width = k + 1
    arr = [0 for _ in range(26)]
    max_freq_letter = letter_no = -1
    for char in s[:width]:
        arr[ord(char) - ord('A')] += 1 #字母出现的次数
    while True:
        for i, letter in enumerate(arr):
            if letter > max_freq_letter:
                max_freq_letter = letter
                letter_no = i
        if width - arr[letter_no] <= k: #需要替换的次数<= k，扩大窗口
            max_len = max(max_len, width)
            if start + width < len(s):
                arr[ord(s[start + width]) - ord('A')] += 1
                width += 1
            else:
                break
        else: #否则缩小窗口
            arr[ord(s[start]) - ord('A')] -= 1
            start += 1
            width -= 1
    return max_len

s=input()
k=input()
print(findmaxlen(s,k))