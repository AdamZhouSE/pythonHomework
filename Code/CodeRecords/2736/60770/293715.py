def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(m):
        op=input().split()
        if op[0]=='Q':
            l, r, k = (map(int, op[1:]))
            part = nums[l - 1:r]
            part.sort()
            print(part[k - 1])
        elif op[0]=='C':
            p,num=map(int,op[1:])
            nums[p-1]=num


if __name__ == '__main__':
    solve()