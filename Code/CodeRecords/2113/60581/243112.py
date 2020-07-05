str = int(input())

count = 0

answer = ""
while str >= 1000:
    part = ""
    left = str%1000
    lst = []
    str = int(str/1000)
    while left > 0:
        lefted = left % 10
        lst.insert(0, lefted)
        left = int(left / 10)
    if lst[0] == 1:
        part += "One Hundred "
    elif lst[0] == 2:
        part += "Two Hundred "
    elif lst[0] == 3:
        part += "Three Hundred "
    elif lst[0] == 4:
        part += "Four Hundred "
    elif lst[0] == 5:
        part += "Five Hundred "
    elif lst[0] == 6:
        part += "Six Hundred "
    elif lst[0] == 7:
        part += "Seven Hundred"
    elif lst[0] == 8:
        part += "Eight Hundred "
    elif lst[0] == 9:
        part += "Nine Hundred "

    if count == 0:
        if lst[1] == 1:
            if lst[2] == 1:
                part += "Eleven"
            elif lst[2] == 2:
                part += "Twelve"
            elif lst[2] == 3:
                part += "Thirteen"
            elif lst[2] == 4:
                part += "Forteen"
            elif lst[2] == 5:
                part += "Fifteen"
            elif lst[2] == 6:
                part += "Sixteen"
            elif lst[2] == 7:
                part += "Seventeen"
            elif lst[2] == 8:
                part += "Eighteen"
            elif lst[2] == 9:
                part += "Ninteen"
            elif lst[2] == 0:
                part += "Ten "
        elif lst[1] == 2:
            part += "Twenty "
        elif lst[1] == 3:
            part += "Thirty "
        elif lst[1] == 4:
            part += "Forty "
        elif lst[1] == 5:
            part += "Fifty "
        elif lst[1] == 6:
            part += "Sixty "
        elif lst[1] == 7:
            part += "Seventy "
        elif lst[1] == 8:
            part += "Eighty "
        elif lst[1] == 9:
            part += "Ninety "

        if lst[1] != 1 and lst[2] == 1:
            part += "One"
        elif lst[1] != 1 and lst[2] == 2:
            part += "Two"
        elif lst[1] != 1 and lst[2] == 3:
            part += "Three"
        elif lst[1] != 1 and lst[2] == 4:
            part += "Four"
        elif lst[1] != 1 and lst[2] == 5:
                part += "Five"
        elif lst[1] != 1 and lst[2] == 6:
            part += "Six"
        elif lst[1] != 1 and lst[2] == 7:
            part += "Seven"
        elif lst[1] != 1 and lst[2] == 8:
            part += "Eight"
        elif lst[1] != 1 and lst[2] == 9:
            part += "Nine"
    else:
        if lst[1] == 1:
            if lst[2] == 1:
                part += "Eleven "
            elif lst[2] == 2:
                part += "Twelve "
            elif lst[2] == 3:
                part += "Thirteen "
            elif lst[2] == 4:
                part += "Forteen "
            elif lst[2] == 5:
                part += "Fifteen "
            elif lst[2] == 6:
                part += "Sixteen "
            elif lst[2] == 7:
                part += "Seventeen"
            elif lst[2] == 8:
                part += "Eighteen "
            elif lst[2] == 9:
                part += "Ninteen "
            elif lst[2] == 0:
                part += "Ten "
        elif lst[1] == 2:
            part += "Twenty "
        elif lst[1] == 3:
            part += "Thirty "
        elif lst[1] == 4:
            part += "Forty "
        elif lst[1] == 5:
            part += "Fifty "
        elif lst[1] == 6:
            part += "Sixty "
        elif lst[1] == 7:
            part += "Seventy "
        elif lst[1] == 8:
            part += "Eighty "
        elif lst[1] == 9:
            part += "Ninety "

        if lst[1] != 1 and lst[2] == 1:
            part += "One "
        elif lst[1] != 1 and lst[2] == 2:
            part += "Two "
        elif lst[1] != 1 and lst[2] == 3:
            part += "Three "
        elif lst[1] != 1 and lst[2] == 4:
            part += "Four "
        elif lst[1] != 1 and lst[2] == 5:
            part += "Five "
        elif lst[1] != 1 and lst[2] == 6:
            part += "Six "
        elif lst[1] != 1 and lst[2] == 7:
            part += "Seven "
        elif lst[1] != 1 and lst[2] == 8:
            part += "Eight "
        elif lst[1] != 1 and lst[2] == 9:
            part += "Nine "

    answer = part + answer
    count += 1
    if count == 1:
        answer = "Thousand " + answer
    elif count == 2:
        answer = "Million " + answer
    elif count == 3:
        answer = "Billion " + answer

lst = []
while str > 0:
    lefted = str % 10
    lst.insert(0, lefted)
    str = int(str / 10)
while len(lst)<3:
    lst.insert(0,0)
part = ""
if lst[0] == 1:
    part += "One Hundred "
elif lst[0] == 2:
    part += "Two Hundred "
elif lst[0] == 3:
    part += "Three Hundred "
elif lst[0] == 4:
    part += "Four Hundred "
elif lst[0] == 5:
    part += "Five Hundred "
elif lst[0] == 6:
    part += "Six Hundred "
elif lst[0] == 7:
    part += "Seven Hundred"
elif lst[0] == 8:
    part += "Eight Hundred "
elif lst[0] == 9:
    part += "Nine Hundred "

if count == 0:
    if lst[1] == 1:
        if lst[2] == 1:
            part += "Eleven"
        elif lst[2] == 2:
            part += "Twelve"
        elif lst[2] == 3:
            part += "Thirteen"
        elif lst[2] == 4:
            part += "Forteen"
        elif lst[2] == 5:
            part += "Fifteen"
        elif lst[2] == 6:
            part += "Sixteen"
        elif lst[2] == 7:
            part += "Seventeen"
        elif lst[2] == 8:
            part += "Eighteen"
        elif lst[2] == 9:
            part += "Ninteen"
        elif lst[2] == 0:
            part += "Ten "
    elif lst[1] == 2:
        part += "Twenty "
    elif lst[1] == 3:
        part += "Thirty "
    elif lst[1] == 4:
        part += "Forty "
    elif lst[1] == 5:
        part += "Fifty "
    elif lst[1] == 6:
        part += "Sixty "
    elif lst[1] == 7:
        part += "Seventy "
    elif lst[1] == 8:
        part += "Eighty "
    elif lst[1] == 9:
        part += "Ninety "

    if lst[1] != 1 and lst[2] == 1:
        part += "One"
    elif lst[1] != 1 and lst[2] == 2:
        part += "Two"
    elif lst[1] != 1 and lst[2] == 3:
        part += "Three"
    elif lst[1] != 1 and lst[2] == 4:
        part += "Four"
    elif lst[1] != 1 and lst[2] == 5:
        part += "Five"
    elif lst[1] != 1 and lst[2] == 6:
        part += "Six"
    elif lst[1] != 1 and lst[2] == 7:
        part += "Seven"
    elif lst[1] != 1 and lst[2] == 8:
        part += "Eight"
    elif lst[1] != 1 and lst[2] == 9:
        part += "Nine"
else:
    if lst[1] == 1:
        if lst[2] == 1:
            part += "Eleven "
        elif lst[2] == 2:
            part += "Twelve "
        elif lst[2] == 3:
            part += "Thirteen "
        elif lst[2] == 4:
            part += "Forteen "
        elif lst[2] == 5:
            part += "Fifteen "
        elif lst[2] == 6:
            part += "Sixteen "
        elif lst[2] == 7:
            part += "Seventeen"
        elif lst[2] == 8:
            part += "Eighteen "
        elif lst[2] == 9:
            part += "Ninteen "
        elif lst[2] == 0:
            part += "Ten "
    elif lst[1] == 2:
        part += "Twenty "
    elif lst[1] == 3:
        part += "Thirty "
    elif lst[1] == 4:
        part += "Forty "
    elif lst[1] == 5:
        part += "Fifty "
    elif lst[1] == 6:
        part += "Sixty "
    elif lst[1] == 7:
        part += "Seventy "
    elif lst[1] == 8:
        part += "Eighty "
    elif lst[1] == 9:
        part += "Ninety "

    if lst[1] != 1 and lst[2] == 1:
        part += "One "
    elif lst[1] != 1 and lst[2] == 2:
        part += "Two "
    elif lst[1] != 1 and lst[2] == 3:
        part += "Three "
    elif lst[1] != 1 and lst[2] == 4:
        part += "Four "
    elif lst[1] != 1 and lst[2] == 5:
        part += "Five "
    elif lst[1] != 1 and lst[2] == 6:
        part += "Six "
    elif lst[1] != 1 and lst[2] == 7:
        part += "Seven "
    elif lst[1] != 1 and lst[2] == 8:
        part += "Eight "
    elif lst[1] != 1 and lst[2] == 9:
        part += "Nine "

answer = part + answer
print(answer)
