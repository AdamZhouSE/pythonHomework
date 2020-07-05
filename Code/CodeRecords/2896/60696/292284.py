if __name__ == '__main__':
    s1 = input()
    s2 = input()
    chars_1 = [0] * 70
    chars_2 = [0] * 70
    for i in range(s1.__len__()):
        chars_1[ord(s1[i])-ord('A')] += 1
    for i in range(s2.__len__()):
        chars_2[ord(s2[i]) - ord('A')] += 1
    flag = True
    for i in range(70):
        if chars_2[i] > chars_1[i]:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')