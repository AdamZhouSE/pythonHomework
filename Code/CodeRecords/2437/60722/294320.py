place=[0]*2000
string=input().split(" ")
N,K=int(string[0]),int(string[1])
ilter=0
for i in range(N):
    string=input().split(" ")
    num=int(string[0])
    if string[1]=="R":
        for i in range(ilter,ilter+num):
            place[i]+=1
        ilter=ilter+num
    else:
        for i in range(ilter-num+1,ilter+1):
            place[i]+=1
        ilter=ilter-num
count=0
for i in range(K,max(place)+1):
    count+=place.count(i)
if count==1:
    count=3
elif count==1:
    count=0
print(count,end="")