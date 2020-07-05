def func12():
    A = list(map(int, input()[1:-1].split(",")))
    B = list(map(int, input()[1:-1].split(",")))
    A_str = "".join("%s" %a for a in A)
    B_str = "".join("%s" %b for b in B)
    if len(A_str) > len(B_str):
        min_str = B_str
        max_str = A_str
    else:
        min_str = A_str
        max_str = B_str
    ans = 0
    flag = False
    for i in range(len(min_str),0,-1):
        for j in range(len(min_str)-i+1):
            if max_str.find(min_str[j:j + i]) != -1:
                ans = i
                flag = True
                break
        if flag:
            break
    print(ans)
    return
func12()