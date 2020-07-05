if __name__=='__main__':
    n = input()
    s = input()
    sr = ""
    for i in range(len(s)):
        sr = sr + chr((ord(s[i])+int(n)-96) % 26+96)
    print(sr,end='')