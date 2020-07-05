def count(year, month, day):
    count = 0
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # print('%d年是闰年，2月份有29天！' % year)
        li1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += li1[i]
        return count + day
    else:
        # print('%d年是平年，2月份有29天！' % year)
        li2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += li2[i]
        return count + day


if __name__ == "__main__":
    x = input().strip().split("-")
    yy = int(x[0])
    mm = int(x[1])
    dd = int(x[2])
    print(count(yy, mm, dd))
