def question21():
    inf = input().split()
    times = int(inf[0])
    lamps = int(inf[1])
    s = set()
    result = set()
    for i in range(1, lamps + 1):
        s.add(i)
    for i in range(0,times):
        inf = input().split()
        for e in inf:
            result.add(int(e))
    if s.__eq__(result):
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    print(question21())