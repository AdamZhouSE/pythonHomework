class Solution(object):
    #Note - this solution may TLE.
    def kthSmallestPrimeFraction(self, A, K):
        pq = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        for _ in range(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        return A[pq[0][1]], A[pq[0][2]]

