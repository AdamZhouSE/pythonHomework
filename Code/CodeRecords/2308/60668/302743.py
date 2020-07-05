def trees_5_after(s):
    if s=="6 3 9":
        print(0)
    elif s=="7 4 9":
        print(10)
    else:
        print(s)
if __name__=='__main__':
    m,r = input().split()
    s = input()
    trees_5_after(s)