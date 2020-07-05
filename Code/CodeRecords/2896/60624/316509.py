def func10():
    s1 = input().strip().split(" ")
    s2 = input().strip().split(" ")
    for i in s2:
        flag = False
        for j in s1:
            if j.find(i) != -1:
                flag = True
        if not flag:
            return False
    return True
if func10():
    print("YES",end="")
else:
    print("NO",end="")