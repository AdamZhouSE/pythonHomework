str=input()
k=int(input())

start=0
end=0
maxi=0
times=[]
for i in range(26): times.append(0)
times[ord(str[end])-ord("A")]+=1
while end<len(str):
    ind=max(times)
    if ind+k>end-start:
        end+=1
        if end<len(str):
            times[ord(str[end])-ord("A")]+=1
    else:
        times[ord(str[start])-ord("A")] -= 1
        start += 1
    if ind+k>maxi:
        maxi=ind+k
print(maxi)