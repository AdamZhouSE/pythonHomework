date = input()
year = int(date[0]+date[1]+date[2]+date[3])
month = int(date[5]+date[6])
days = int(date[8]+date[9])
total = days
leap = False
if(year%4 == 0 and year%100 != 0):
    leap = True
elif(year%100 ==0 and year %400==0):
    leap ==True

for i in range(1,month):
    if(i == 2):
        if(leap):
            total += 29
        else:
            total += 28
    elif(i <=7):
        if(i %2==0):
            total +=30
        else:
            total +=31
    else:
        if(i %2==0):
            total +=31
        else:
            total +=30            
print(total)