l=[]
l.append(input())
l.append(input())
request=l[0].split()
buckets=l[1].split()
garden=int(request[1])
for i in range(int(request[0])-1,-1,-1):
    if garden%int(buckets[i])==0:
        print(garden//int(buckets[i]))
        break