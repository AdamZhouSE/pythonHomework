def solve(string, a):
    alphbet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    a1 = "A"
    if a == 1:
        return a1
    else:
        res = solve(string,a-1)
        return res + alphbet[a-1] + res


num = int(input())
print(solve("",num))
