def decodeString(s: str) -> str:
    # Initialize data structure
    stack, res, num = [], '', 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c.isalpha():
            res += c
        elif c == '[':
            # Tuple form stacking
            stack.append((res, num))
            # Refresh strings and number of repetitions
            res, num = '', 0
        else:
            # If c==']', pop-up strings and number of repetitions
            last_str, this_num = stack.pop()
            res = last_str + this_num * res
    return res


n=int(input())
ans=[]
for i in range(0,n):
    ans.append(decodeString(input()))

for i in ans:
    print(i)