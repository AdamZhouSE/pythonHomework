def solve(num):
    #num=list(map(int,num))
    m=sorted(num)
    target=m[0]
    return target
if __name__ == '__main__':
    num=eval(input())
    print(solve(num))