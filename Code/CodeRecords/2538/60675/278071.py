def func(arr):

    l = list(range(10000))
    for i in range(len(arr)):
        if arr[i] in l:
            l.remove(arr[i])
    if (l[0] == 0):
        print(l[1])
    else:
        print(l[0])



n = "l = " + input()
exec(n)
func(l)