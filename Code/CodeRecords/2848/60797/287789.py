class Solution:
    def find(self, nA, nB, k, m, A, B):
        if A[k-1] < B[-m]:
            return 'YES'
        else:
            return 'NO'
if __name__ == '__main__':
    tmp = input().split()
    nA = int(tmp[0])
    nB = int(tmp[1])
    tmp = input().split()
    k = int(tmp[0])
    m = int(tmp[1])
    A = [int(a) for a in input().split()]
    B = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(nA, nB, k, m, A, B)
    print(re)
