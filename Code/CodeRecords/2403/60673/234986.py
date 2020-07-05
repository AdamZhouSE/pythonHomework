candies = int(input())
num_people = int(input())
itr = 0;
res = []
while(itr<num_people):
    res.append(0)
    itr+=1
itr = 0
onetime = 1
while(candies!=0):
    if(itr==num_people):
        itr = 0
    res[itr] += onetime
    candies = candies - onetime
    onetime += 1
    if(candies<onetime):
        onetime = candies
    itr += 1
print (res)