candies=int(input())
people=int(input())
num=[]*people
time=0
candy=1
if (1+2**n)*(2**n)//2>candies:
    while candies>0 :
        if candies>candy:
            num[time%people]+=candies
            break
        else:
            num[time%people]+=candy
            candies-=candy
            time+=1
            candy+=1
print(num)
        