if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        st = set(s)
        d = {}
        for a in s:
            d[a] = s.count(a)
        if 'a' in d.keys():
            del d['a']
        if 'e' in d.keys():
            del d['e']
        if 'i' in d.keys():
            del d['i']
        if 'o' in d.keys():
            del d['o']
        if 'u' in d.keys():
            del d['u']
        res = len(d)
        if res%2==1:
            print('HE!')
        else:
            print('SHE!')
