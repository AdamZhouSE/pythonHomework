def bl(x,n):
    r=str(x**n)
    if len(r.split('.')[1])<5:
        r+='0'*(5-len(r.split('.')[1]))
    print(r)

if __name__ == '__main__':
    bl(float(input()),int(input()))
