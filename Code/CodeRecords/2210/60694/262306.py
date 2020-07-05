# www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string

no_of_chars = 256
def findSubString(string, pat):
    len1, len2 = len(string), len(pat)
    hash_pat, hash_str = [0] * no_of_chars, [0] * no_of_chars

    # store occurrence of characters of pattern
    for i in range(len2):
        hash_pat[ord(pat[i])] += 1

    start, start_index, min_len = 0, -1, float('inf')

    # start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1

        # If string's char matches with
        # pattern's char then increment count
        if hash_pat[ord(string[j])] != 0 and hash_str[ord(string[j])] <= hash_pat[ord(string[j])]:
            count += 1

        if count == len2:
            # Try to minimize the window i.e., check if
            # any character is occurring more no. of times
            # than its occurrence in pattern, if yes
            # then remove it from starting and also remove
            # the useless characters.
            while (hash_str[ord(string[start])] >
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):

                if (hash_str[ord(string[start])] >
                        hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1

            # update window size
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start

    return string[start_index: start_index + min_len]


T = int(input())
for _ in range(T):
    S, text = input(), input()
    if len(set(S) & set(text)) != len(text):
        print(-1)
        continue
    print(findSubString(S, text))

