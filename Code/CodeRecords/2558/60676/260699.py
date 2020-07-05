def reverse(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '{':
            stack.append('{')
        else:
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop(-1)
            else:
                stack.append('}')
    if len(stack) % 2 == 1:
        return -1
    if stack.count('{') % 2 == 1:
        return len(stack) // 2 + 1
    return len(stack) // 2


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(reverse(input()))
    for i in range(len(result)):
        print(result[i])