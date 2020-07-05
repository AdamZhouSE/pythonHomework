count=int(input())
survival=[]
while count>0:
   n,k=map(int,input().split())
   people=[i for i in range(1,n+1)]
   step=k-1
   start=0
   while len(people)>1:
       people.remove(people[start+step])
       start=start+step
       while start+step>=len(people):
           start=start-len(people)
   count=count-1
   survival.append(people[0])
for i in survival:
    print(i)