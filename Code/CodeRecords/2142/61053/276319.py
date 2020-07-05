def parenthesis(str):
    lst = []
    total = 0
    ans = []
    for ch in str:
        if ch == '(':
            total += 1
            ans.append(total)
            lst.append(total)
        elif ch == ')':
            ans.append(lst.pop())
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(parenthesis(str))
    for res in ans:
        for no in res:
            print(no,end=" ")
        print()