s1 = input()
s2 = input()
else:
    count = 0
    for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            for k in range(len(s2)-(j-i)+1):
                if s1[i:j] == s2[k:k+j-i]:
                    count = count + 1
    print(count,end ="")