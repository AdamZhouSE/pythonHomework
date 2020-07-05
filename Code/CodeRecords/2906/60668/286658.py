if __name__=='__main__':
    n = input()
    s = input()
    sr = ""
    for i in range(len(s)):
        sr = sr + chr((ord(s[i])+int(n))%26)
    print(sr,end='')