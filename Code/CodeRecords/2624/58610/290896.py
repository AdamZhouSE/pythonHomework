def diff_ways_to_compute(s: str):
    if s.isdigit():
        return [int(s)]
    res = []
    for i, char in enumerate(s):
        if char in ['+', '-', '*']:
            left = diff_ways_to_compute(s[:i])
            right = diff_ways_to_compute(s[i + 1:])
            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res

print(diff_ways_to_compute(input()))