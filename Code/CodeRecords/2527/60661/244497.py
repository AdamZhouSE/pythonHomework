rests=input()[2:-2].split('],[')
for i in range(len(rests)):
    rests[i]=rests[i].split(',')
    rests[i]=[int(x) for x in rests[i]]
vegan=int(input())
maxPrice=int(input())
maxDistance=int(input())
left=[]
for i in range(len(rests)):
    if rests[i][2]>=vegan and rests[i][3]<=maxPrice and rests[i][4]<=maxDistance:
        left.append(rests[i])
left.sort(key=lambda x:x[1])
left.reverse()
#if [x[0] for x in left]==[4,3,5]:
#    print(rests,vegan,maxPrice,maxDistance)
print([x[0] for x in left])

