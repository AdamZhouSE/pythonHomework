def func(arr):
    tmp = arr.copy()
    tmp.sort()
    print("[",end="")
    for i in range(len(tmp)):
        if i == 0:
            print(tmp[0],end="")
        else:
            print(", ",end="")
            print(tmp[i],end="")
    print("]")



n = "l = " + input()
exec(n)
func(l)
