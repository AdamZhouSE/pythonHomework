def match_longest_parentheses(s):
    size = len(s)
    li = []  
    deep = 0 
    start = 0  
    for i in range(size):
        if s[i] == '(':
            deep += 1
        else:  # s[i] == ')'
            deep -= 1
            if deep == 0:
                if len(li) == 0 or li[0][1] - li[0][0] < i - start:
                    li = [[start, i]]
                elif li[0][1] - li[0][0] == i - start:
                    li.append([start, i])
            elif deep < 0:  
                deep = 0
                start = i + 1