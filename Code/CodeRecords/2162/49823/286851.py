def bl(x,n):
    print(str(x**n)+'0'*(5-len(str(x**n)[2:])))
if __name__ == '__main__':
    bl(float(input()),int(input()))
