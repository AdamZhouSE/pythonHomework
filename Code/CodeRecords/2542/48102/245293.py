def long_seq(ls: list) -> int:
    num_set = set(ls)
    max_long = 0
    for i in num_set:
        if i - 1 not in num_set:
            curr = i
            curr_long = 1
            while curr + 1 in num_set:
                curr += 1
                curr_long += 1
            max_long = max(max_long, curr_long)
    return max_long


lst = eval(input())
print(long_seq(lst))