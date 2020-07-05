def linerlist_16_find(n):
    for i in range(n):
        if pow(i,2)>=n:
            return pow(i,2)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        print(linerlist_16_find(int(n)))