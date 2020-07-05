class Solution:
    def find(self, data, n):
        if len(data)==0:
            return 0
        p = []
        count = 0
        #global dbg
        #dbg = [] # debug
        while True:
            q = []
            for i in range(len(data)):
                tmp = data[i]
                if len(p)!=0:
                    for item in p:
                        tmp += item
                        if int(tmp) <= n:
                            #dbg.append(tmp) # debug
                            count += 1
                            q.append(tmp)
                            tmp = tmp[:len(tmp)-len(item)]
                        else:
                            return count
                else:
                    if int(tmp) <= n:
                        #dbg.append(tmp)  # debug
                        count += 1
                        q.append(tmp)
                    else:
                        return count
            p = q

if __name__ == '__main__':
    data = input().split(',')
    n = int(input())
    s = Solution()
    re = s.find(data, n)
    print(re)
    #global dbg
    #print(dbg)