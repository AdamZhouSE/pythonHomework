def ok(sub_string):
    chars = [0] * 30
    for i in range(len(sub_string)):
        chars[ord(sub_string[i])-ord('a')] += 1
    cnt = 0
    for i in range(30):
        if chars[i] != 0:
            cnt += 1
    if cnt <= maxLetters:
        return True
    else:
        return False


if __name__ == '__main__':
    s = input()
    n = len(s)
    maxLetters = int(input())
    min_size = int(input())
    max_size = int(input())
    # sub_strings = [s[i:i+l] for l in range(min_size, max_size+1) for i in range(n-l+1)]
    sub_strings = dict()
    for l in range(min_size, max_size+1):
        for i in range(n-l+1):
            if ok(s[i:i+l]):
                if sub_strings.get(s[i:i + l]) is None:
                    sub_strings[s[i:i+l]] = 1
                else:
                    sub_strings[s[i:i+l]] += 1
    print(max(sub_strings.values()))