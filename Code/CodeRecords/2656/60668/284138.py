def linerlist_17_diff(M,N):
    str_M = M[2:]
    str_N = N[2:]
    co = 0
    if str_M == str_N:
        return -1
    if len(str_M)>len(str_N):
        str_N = "0"*(len(str_M)-len(str_N)) + str_N
    elif len(str_M)<len(str_N):
        str_M = "0"*(len(str_N)-len(str_M)) + str_M
    for i in range(len(str_N)-1,0,-1):
        if str_M[i] != str_N[i]:
            co = len(str_N)-i
            break
    return co
if __name__=='__main__':
    for _ in range(int(input())):
        M,N = input().split()
        print(linerlist_17_diff(bin(int(M)),bin(int(N))))