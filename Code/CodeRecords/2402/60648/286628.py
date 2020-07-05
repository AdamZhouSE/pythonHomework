from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for l, r, seat in bookings:
            res[l - 1] += seat
            if r < n:
                res[r] -= seat
        for i in range(1,n):
            res[i] += res[i - 1]
        return res


if __name__=="__main__":
    n=int(input())
    ls=[]
    for i in range(n):
        ls.append(eval('['+input()+']'))
    m=int(input())
    x=Solution().corpFlightBookings(ls,m)
    print(x)