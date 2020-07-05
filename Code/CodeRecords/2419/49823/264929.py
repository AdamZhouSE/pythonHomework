def aj(n):
    a,b=1,0
    for i in range(0,len(str(n))):
        a*=int(str(n)[i])
        b+=int(str(n)[i])
    print(a-b)
if __name__ == '__main__':
    aj(int(input()))
