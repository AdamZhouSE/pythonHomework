def numop1():
    candies=int(input())
    num_people=int(input())
    people=[0]*num_people
    count=0
    while(candies>0):

        for i in range(0,len(people)):
            if(candies>=count*len(people)+i+1):
                people[i]+=count*len(people)+i+1
                candies-=count*len(people)+i+1
            elif(candies>0):
                people[i]+=candies
                candies=0
            elif(candies==0):
                break
        count+=1
    print(people)
    return

numop1()