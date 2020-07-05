def bl(x,n):
    print(str(x**n)+'' if len(str(x**n)[2:])<5 else '0'*(5-len(str(x**n)[2:])))
if __name__ == '__main__':
    bl(float(input()),int(input()))
