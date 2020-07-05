ls = list(input().split("-"))
year = int(ls[0])
month = int(ls[1])
date = int(ls[2])
bissextile = [31,60,91,121,152,182,213,244,274,305,335,366]    #leap year
commonYear =[31,59,90,120,151,181,212,243,273,304,334,365]
enterYear = year
enterMonth = month
enterDay = date
remained = 0
# first need to check is leap or common year
if (enterYear%100 !=0) and (enterYear %4 == 0 ) or (enterYear%400 == 0):
    if enterMonth > 1 :
        remained = bissextile[enterMonth-1] + enterDay
    else:
        remained = enterDay
else:
    if enterMonth > 1 :
        remained = commonYear[enterMonth-1] + enterDay
    else:
        remained = enterDay
print(remained)