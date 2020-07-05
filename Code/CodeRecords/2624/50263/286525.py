def compute(m):
    if m.isdigit():
        return [int(m)]
    result = []
    for i, char in enumerate(m):
        if char in ['+', '-', '*']:
            left = compute(m[:i])
            right = compute(m[i+1:])
            for l in left:
                for r in right:
                    if char == '+':
                        result.append(l+r)
                    elif char == '-':
                        result.append(l-r)
                    else:
                        result.append(l*r)
    return result


if __name__ == "__main__":
    m = input()
    print(compute(m))