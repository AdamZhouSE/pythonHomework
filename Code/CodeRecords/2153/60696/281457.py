def solve(n):
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)
    original = bin(n).replace('0b', '')
    dest = '0b'
    for i in range(len(original)):
        if original[i] == '0':
            dest += '1'
        else:
            dest += '0'
    res = int(dest, 2)
    print(res)
    
    
if __name__ == '__main__':
    n = int(input())
    solve(n)