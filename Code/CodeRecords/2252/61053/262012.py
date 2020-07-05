def find_word(s,c):
    start = 0
    c_len = len(c)
    s_len = len(s)
    c_dict = {}
    for ch in c:
        if ch in c_dict:
            c_dict[ch] = c_dict[ch] + 1
        else:
            c_dict[ch] = 1
    count = 0
    while start <= s_len - c_len:
        new_dict = c_dict.copy()
        same = True
        for ch in s[start:start+c_len]:
            if not ch in new_dict:
                same = False
                break
            if ch in new_dict:
                new_dict[ch] = new_dict[ch] - 1
                if new_dict[ch] < 0:
                    same = False
                    break
        if same:
            count = count + 1
        start = start + 1
    return count

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        s = input()
        c = input()
        ans.append(find_word(s,c))
    for res in ans:
        print(res)