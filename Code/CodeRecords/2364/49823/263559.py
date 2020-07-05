def af(n):
    r=0
    for i in range(1,n+1):
        if len(str(i))!=len(set(str(i))):
            r+=1
    print(r)
if __name__ == '__main__':
    af(int(input()))
