#最小好进制数
# #实现从十进制到b进制的转换
def hashFuc(x, y):
    if y < 10:
        z = []
        while x != 0:
            z.append(x % y)
            x = x // y
        result = z[::-1]
    else:
        k = []
        z = []
        while x != 0:
            z.append(x % y)
            x = x // y
        for i in range(len(z)):
            if z[i] >= 10:
                z[i] = z[i] - 10 + ord('A')
            elif z[i] <= 9 and z[i] >= 0:
                z[i] = z[i] + ord('0')
        for i in range(len(z)):
            k.append(chr(z[i]))
        result = k[::-1]

    #for i in range(len(result)):
        #s=s+result[i]
    return ''.join(str(j) for j in result)

def solve(num):
    c=2
    while True:
        any=hashFuc(num,c)
        p=list(any)
        if p.count('1')==len(p):
            return c
        c=c+1

if __name__ == '__main__':
    a=int(input())
    print(solve(a))