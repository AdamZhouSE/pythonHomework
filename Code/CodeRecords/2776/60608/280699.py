
def func6():
    words = eval(input())
    strarr, ans = sorted(words, key=lambda x: len(x)), []
    s = set(strarr)
    while strarr:
        word = strarr.pop(-1)
        s.remove(word)
        length, stack = len(word), [0]
        while stack:
            p, flag = stack.pop(0), False
            for i in range(p + 1, length + 1):
                if word[p:i] in s:
                    stack.append(i)
                    if i == length:
                        ans.append(word)
                        flag = True
                        break
                if flag:
                    break
    res = []
    for item in words:
        if item in ans:
            res.append(item)
    print(res)


func6()
