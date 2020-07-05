def linerlist_21_oe(n):
    n = n[2:]
    co = 0
    for i in range(len(n)):
        if n[i]=='1':
            co+=1
    if co%2==0:
        print("even")
    else:
        print("odd")
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_21_oe(bin(int(n)))