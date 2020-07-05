class Solution(object):
    def peakIndexInMountainArray(self, A):
        for i in xrange(len(A)):
            if A[i] > A[i+1]:
                return i

