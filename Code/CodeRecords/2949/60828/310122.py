def h5():
    s = list(input().split())
    s.remove(s[len(s)-1])
    res = ""
    for i in range(len(s)-1,0,-1):
        res += s[i]+" "
    res += s[0]
    print(res,end="")
if __name__ == '__main__':
    h5()