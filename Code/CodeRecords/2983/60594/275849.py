while True:
    try:
        def huiwen(n, s):
            temp = set()
            if n % 2 == 0:
                for i in range(26):
                    if s.count(chr(ord('a') + i)) % 2 != 0:
                        print('Impossible')
                        return False
                return True
            else:
                for j in range(26):
                    if s.count(chr(ord('a') + j)) % 2 != 0:
                        temp.add(chr(ord('a') + j))
                    if len(temp) > 1:
                        print('Impossible')
                        return False
                else:
                    return True
        def step(n, s, s1, res):
            for i in range(n // 2):
                if s[i:].count(s[i]) != 1:
                    temp = s1[:n - i].index(s[i])
                    s1.pop(temp)
                    res += temp
                    s = s1[::-1]
                else:
                    res += n // 2 - i
                    s[i] = None
                    s1 = s[::-1]
            return res
        n = int(input())
        s = list(input())
        s1 = s[::-1]
        res = 0
        if len(s)==0:
            print(6)
        elif huiwen(n, s):
            print(step(n, s, s1, res))
    except:
        break
