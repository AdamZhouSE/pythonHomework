def inc(val):
    carry = True
    for i in range(len(val)-1,-1,-1):
        if carry:
            val[i] = chr(ord(val[i])+1)
            if val[i] > 'Z':
                carry = True
                val[i] = 'A'
            else:
                carry = False
    if carry:
        val.insert(0,'A')
    return val

def f(n):
    val = []
    for i in range(n):
        inc(val)
    print("".join(val))
    return val

if __name__ == "__main__":
    n = int(input())
    f(n)