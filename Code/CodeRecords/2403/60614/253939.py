candies=int(input())
num=int(input())
people=[0]*num
init=0
i=1
while candies>0:
    if candies<init*num+i:
        people[i-1]+=candies
        break
    else:
        people[i-1]+=init*num+i
        candies-=init*4+i
        if i<num:
            i+=1
        else:
            i=1
            init+=1
print(people)