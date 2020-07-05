def parenthesis(str):
    total = 0
    left = 0
    ans = []
    for ch in str:
        if ch == '(':
            total += 1
            left = total
            ans.append(total)
        elif ch == ')':
            ans.append(left)
            left -= 1
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(parenthesis(str))
    for res in ans:
        print(*res)