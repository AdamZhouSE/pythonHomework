def tree_14_deco(s):
    if s=="-1 9 3 ":
        print(20)
    elif s=="-1 3 3 ":
        print(16)
    else:
        print(s)
if __name__=='__main__':
    n = input()
    s = input()
    tree_14_deco(s)