class Solution:
    def corpFlightBookings(self, bookings, n: int):
        segmentsArr = []
        for i in range(len(bookings)):
            start, end, tickets = bookings[i];
            segmentsArr.append([start, tickets])
            segmentsArr.append([end + 1, -tickets])  # 防止后续需要两个while处理正负情况

        segmentsArr = sorted(segmentsArr)

        index, count, ans = 0, 0, [0] * n
        for i in range(n):
            while index < len(segmentsArr) and segmentsArr[index][0] <= i + 1:
                count += segmentsArr[index][1]
                index += 1
            ans[i] = count
        return ans
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
a = int(input())
s = Solution()
print(s.corpFlightBookings(n,a))
