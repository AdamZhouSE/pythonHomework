def compute(exp):
    all_res = []
    for i in range(len(exp)):
        c = exp[i]
        if c == "+" or c == "-" or c == "*":
            left = exp[:i]
            right = exp[i+1:]
            left = compute(left)
            right = compute(right)
            for i in range(len(left)):
                for j in range(len(right)):
                    if c == "+":
                        all_res.append(left[i]+right[j])
                    elif c == "-":
                        all_res.append(left[i]-right[j])
                    elif c == "*":
                        all_res.append(left[i]*right[j])
    if len(all_res) == 0:
        all_res.append(int(exp))
    return all_res


exp = input()
res = compute(exp)
print(res)