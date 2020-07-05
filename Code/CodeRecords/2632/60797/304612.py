class Solution:
    def find(self, n, msg):
        house = [1 for i in range(n)]
        l = []
        for m in mesg:
            if m[0] == 'D':
                p = int(m[1]) - 1
                l.append(p)
                house[p] = 0
            elif m[0] == 'Q':
                count = 0
                p = int(m[1]) - 1
                while p != -1 and house[p] != 0:
                    count += 1
                    p -= 1
                p = int(m[1]) - 1
                while p != len(house) and house[p] != 0:
                    if p == int(m[1]) - 1:
                        p+=1
                        continue
                    count += 1
                    p += 1
                print(count)
            elif m[0] == 'R':

                house[l.pop()] = 1


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]

    mesg = []
    for i in range(n):
        mesg.append(input().split())
    s = Solution()
    res = s.find(n, mesg)
    print(res, end='')
