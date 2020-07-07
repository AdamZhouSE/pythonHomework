class Solution:
    def threeEqualParts(self, A):
        n = A.count(1)
        if n == 0:
            return([0,len(A)-1])
        else:
            if n%3 !=0:
                return([-1,-1])
            else:
                j = 0
                for i in range(0,len(A)):
                    if A[i] == 1:
                        j = j + 1
                        if j == 1:
                            x = i
                        if j == n/3 + 1:
                            y = i
                        if j == (2*n)/3 + 1:
                            z = i
                Z = A[z:len(A)]
                m = len(Z)
                if y - x >= m and z - y >= m:
                    Y = A[y:y + m]
                    X = A[x:x + m]
                else:
                    return([-1,-1])
                if Z==X and Z==Y:
                    return([x+m-1,y+m])
                else:
                    return([-1,-1])
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.threeEqualParts(c))