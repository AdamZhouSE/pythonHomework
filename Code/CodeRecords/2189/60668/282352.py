def isHappy(n):
    isam = [n]
    while n!=1:
        a = list(str(n))
        n = 0
        for i in a:
            n+=pow(int(i),2)
        isam.append(n)
        if len(isam) != len(set(isam)):
            return False
    return True
def linerlist_3_findHappy(n):
    co = n+1
    while not isHappy(co):
        co+=1
    print(co)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_3_findHappy(int(n))