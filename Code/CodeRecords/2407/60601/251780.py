import datetime


def dayOfYear(date: str) -> int:
    Y, M, D = list(map(int, date.split("-")))
    return int(datetime.date(Y, M, D).strftime("%j"))

date = input()
print(dayOfYear(date))