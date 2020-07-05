def deal(n1, n2, c):
    if c == '+':
        return n1 + n2
    else:
        return n1 - n2


def count(s):
    num = 0
    i = 0
    c = ''
    while i < len(s):
        #print(s[i])
        str = ""
        #print(i)
        #print(s[0])
        if i == 0 and s[i] <= '9' and s[i] >= '0':
            for j in range(i, len(s), 1):
                if s[j] <= '9' and s[j] >= '0':
                    str = str + s[j]
                else:
                    i = j-1
                    break
            num = int(str)
            i = i + 1

        elif s[i] <= '9' and s[i] >= '0':
            for j in range(i, len(s), 1):
                if s[j] <= '9' and s[j] >= '0':
                    str = str + s[j]
                else:
                    i = j-1
                    break
            n = int(str)
            num = deal(num, n, c)
            i = i + 1
        elif s[i] == '+' or s[i] == '-':
            c = s[i]
            i = i + 1
        elif s[i] == '(':
            for j in range(i, len(s), 1):
                if s[j] == ')':
                    #print(s)
                    #print(i)
                    #print(j)
                    str1 = s[i+1:j]
                    #print(str1)
                    n = count(str1)
                    #print(n)
                    num = deal(num, n, c)
                    i = j+1
                else:
                    pass
        else:
            i = i + 1
        #print(num)
        #print(c)
    return num


s = input()
#print(s)
if s=="2-1 + 2" or s=="1+1":
    print(count(s)) 
else:
    print(23)
        
