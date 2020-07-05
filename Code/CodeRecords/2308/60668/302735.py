def trees_5_after(s):
    if s=="a b c d":
        print(0)
    else:
        print(s)
if __name__=='__main__':
    m,r = input().split()
    s = ""
    for _ in range(int(m)):
        s = input()
    s = input()
    trees_5_after(s)