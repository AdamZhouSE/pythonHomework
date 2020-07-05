def max_string(given_str: str, strings: list) -> str:
    chars = [0] * 30
    strings.sort(key=lambda x: (-len(x), x))
    for i in range(len(given_str)):
        chars[ord(given_str[i])-ord('a')] += 1
    for string in strings:
        temp = [0] * 30
        for i in range(len(string)):
            temp[ord(string[i])-ord('a')] += 1
        flag = True
        for i in range(30):
            if chars[i] < temp[i]:
                flag = False
                break
        if flag:
            return string
    return ''


if __name__ == '__main__':
    given_str = input()
    strings = eval(input())
    print(max_string(given_str, strings))
