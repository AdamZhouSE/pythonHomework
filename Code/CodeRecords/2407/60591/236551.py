s = input()
date = list(map(int,s.split("-")))
result = date[2]
for m in range(1,date[1]):
    temp = m
    if(temp == 1 or temp == 3 or temp == 5 or temp == 7 or temp == 8 or temp == 10 or temp == 12):
        result += 31
    elif(temp == 2):
        if((date[0]%100!=0 and date[0]%4==0) or (date[0]%400==0)):
            result += 29
        else:
            result += 28
    else:
        result += 30

print(result)