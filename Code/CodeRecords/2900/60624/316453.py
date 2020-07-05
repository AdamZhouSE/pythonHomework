def func13():
    s = input().strip()
    ans = len(s)
    for i in s:
        if i==" " or i=="\n":
            ans -= 1
    print(ans,end="")
    return 
func13()