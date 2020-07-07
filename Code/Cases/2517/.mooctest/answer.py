class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        ab_map = dict()

        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1

        for c in C:
            for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]

        return count
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))

b3 = input().split(',')
c3= []
for i in b3:
    c3.append(int(i))
    
b4 = input().split(',')
c4= []
for i in b4:
    c4.append(int(i))
s = Solution()
print(s.fourSumCount(c1,c2,c3,c4))

