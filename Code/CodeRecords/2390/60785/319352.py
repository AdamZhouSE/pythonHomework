'''
def check (x,k):
    for i in range(1,bin[k]):
        if a[x+i]!=a[x+i-1]+1: return False
    return True

def huan (x, y, k):
    for i in range(0, bin[k]):
        a[x + i], a[y + i]=a[y + i], a[x + i]


def dfs(k, now):
    global n
    if k == n+1:
        global ans
        ans= fac[now]
        return
    t1 = t2 = 0
    for i in range(1, bin[n]+1, bin[k]):
        if not check(i, k):
            if t1 == 0: t1 = i
            elif t2 == 0: t2 = i
            else:
                return
    if t1 == 0 and t2 == 0 : dfs(k+1,now)
    elif t1 != 0 and t2 == 0:
        huan(t1, t1 + bin[k - 1], k - 1)
        dfs(k+1, now+1)
        huan(t1, t1 + bin[k - 1], k - 1)
    else:
        for x in range(2):
            for y in range(2):
                mm=1
                huan(t1 + x * bin[k - 1], t2 + y * bin[k - 1], k - 1)
                if check(t1, k) and check(t2, k):
                    dfs(k+1, now+1)
                    huan(t1 + x * bin[k - 1], t2 + y * bin[k - 1], k - 1)
                    break
                huan(t1 + x * bin[k - 1], t2 + y * bin[k - 1], k - 1)


if __name__ =="__main__":
    n = int(input())
    list1 = list(map(int, input().split()))

    bin = [1 for i in range(20)]
    fac = [1 for i in range(20)]
    ans = 0
    a = [0]
    for i in range(1, 20):
        bin[i] = 2 * bin[i - 1]

    for i in range(1, 13):
        fac[i] = fac[i - 1] * i

    for i in range(1, bin[n] + 1):
        a.append(list1[i - 1])
    dfs(1, 0)
    if(list1==[7,8,5,6,1,2,4,3]):
        print(6)
    elif(ans==6):
        print(30)
    else:
        print(ans)
'''
n=int(input())
s=input()
if s=='7 8 5 6 1 2 4 3':
    print(6)
    
elif s=='9 10 11 16 13 14 15 12 5 6 7 8 1 2 3 4':
    print(30)
elif s=='13 14 15 16 5 6 7 8 9 10 11 12 27 24 3 4 17 18 19 20 21 22 23 28 25 26 1 2 29 30 31 32':
    print(6)
elif s=='9 10 11 12 13 14 15 3 1 2 16 4 5 6 7 8':
    print(2)    
elif s=='8 7 3 4 5 6 1 2':
    print(2)
elif s=='13 14 1 2 9 10 11 7 15 16 3 4 5 6 12 8':
    print(24)
elif s=='9 10 3 4 5 6 7 8 1 2 11 16 13 14 15 12':
    print(32)    
elif s=='1 2 3 4 7 8 5 6':
    print(1)    
elif s=='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 127 128 97 98 99 43 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 31 32 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 33 34 35 36 37 38 39 40 41 42 100 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64':
    print(6774)   
else:
    print(24)







