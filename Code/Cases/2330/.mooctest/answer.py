class Solution:
    def minAreaFreeRect(self, points) -> float:
        n = len(points)
        ans = float('inf')
        record = {}
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                center = ((x1+x2)/2,(y1+y2)/2)
                length = (x1-x2)**2+(y1-y2)**2
                if (center,length) in record:
                    for m in record[(center,length)]:
                        x3,y3 = m
                        ans = min(ans,(((x1-x3)**2+(y1-y3)**2)**0.5)*(((x2-x3)**2+(y2-y3)**2)**0.5))
                    record[(center,length)].append(points[i])
                    record[(center,length)].append(points[j])
                else:
                    record[(center,length)] = [points[i],points[j]]
        return ans if ans!=float('inf') else 0
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print("%.4f" % s.minAreaFreeRect(n))
