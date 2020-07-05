class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int,date.split('-'))
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year%4==0 and year%100!=0) or (year%400==0) : months[2] += 1
        res = 0
        for i in range(month): res += months[i]
        res += day
        return res
        

if __name__=="__main__":
    s=input()
    x=Solution().dayOfYear(s)
    print(x)