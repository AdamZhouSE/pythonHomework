s = input()
for n in range(1, len(s)+1):
    ss = s[:n]
    m = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for len in range(j-i+1, n-j+2):
                if ss[i-1:i+len-1] == ss[j-1:j+len-1]:
                    m += len
    print(m % (pow(10,9) + 7))