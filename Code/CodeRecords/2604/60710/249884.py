def solve(l,t):
    for i in l:
        if i>t:
            return i
    return l[2]
if __name__ == '__main__':
    l=input()
    t=input()
    print(solve(l,t))