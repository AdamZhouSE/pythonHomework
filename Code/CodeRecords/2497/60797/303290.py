class Solution:
    def find(self, target, pos, sp):
        d={}
        for i in range(len(pos)):
            d[pos[i]]=sp[i]
        sorted(d.items(), key=lambda x:x[1])
        t = []
        for i in range(len(pos)):
            t.append((target-pos[i])/sp[i])
        cur = t[0]
        re = 0
        for i in range(1,len(t)):
            if cur>t[i]:
                re+=1
                continue
            else:
                cur = t[i]
        return re

if __name__ == '__main__':
    target = int(input())
    pos = [int(a) for a in input().strip('[]').split(',')]
    sp = [int(a) for a in input().strip('[]').split(',')]
    s = Solution()
    res = s.find(target, pos, sp)
    print(res)

