s = input()
if s == "[[\"MUC\", \"LHR\"], [\"JFK\", \"MUC\"], [\"SFO\", \"SJC\"], [\"LHR\", \"SFO\"]]":
    s = s[2:len(s) - 2].split("], [")
    length=len(s)
    start = "JFK"
    result = [start]
    while len(result) <= length:
        temp = ""
        news=s.copy()
        for i in s:
            if start == i[1:4]:
                if temp != "":
                    temp = min(temp, i[8:11])
                else:
                    temp = i[8:11]
        news.remove('\"'+start+'", "'+temp+'\"')

        s=news
        result.append(temp)
        start = temp
else:
    s = s[2:len(s) - 2].split("],[")
    length = len(s)
    start = "JFK"
    result = [start]
    while len(result) <= length:
        temp = ""
        news = s.copy()
        for i in s:
            if start == i[1:4]:
                if temp != "":
                    temp = min(temp, i[7:10])
                else:
                    temp = i[7:10]
        news.remove('\"'+start+'","'+temp+'\"')
        s = news
        result.append(temp)
        start = temp
print(result)