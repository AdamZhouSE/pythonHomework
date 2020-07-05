def solve(n):
    a=n**0.5
    #print(a)
    b=int(n**0.5)
    return str(a)==str(b)
if __name__ == '__main__':
    a=int(input())
    print(solve(a))