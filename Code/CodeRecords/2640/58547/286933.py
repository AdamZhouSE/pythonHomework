def check_window(needs, window):
    for k in needs.keys():
        if k not in window or window.get(k, -1) < needs[k]:
            return False
    return True


def func():
    origin_str = input()
    target = input()

    res = ""
    if not target or len(origin_str) < len(target):
        return ""

    left, right = 0, 0
    needs = {}  # target dict
    window = {}  # now window
    
    for c in target:
        needs[c] = 1 if c not in needs else needs[c] + 1
        
    while right < len(origin_str):
        window[origin_str[right]] = 1 if origin_str[right] not in window else window[origin_str[right]] + 1
        while check_window(needs, window):
            # print(needs, window)
            if len(res) > len(origin_str[left: right + 1]) or not res:
                res = origin_str[left: right + 1]
            window[origin_str[left]] -= 1
            left += 1

        right += 1

    print(res)


func()
