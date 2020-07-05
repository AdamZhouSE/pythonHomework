def solve(num):
    s=str(num)
    if num<0:
        s1=s[1:]
        s2=s1[::-1]
        s3='-'+s2
        return int(s3)
    s1=s[::-1]
    return int(s1)
if __name__ == '__main__':
    a=int(input())
    print(solve(a))
