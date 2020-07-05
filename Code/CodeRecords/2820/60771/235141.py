#5
n = int(input())
hour = []
minute = []
server = 1
for i in range(0,n):
    l = input().split(" ")
    hour.append(int(l[0]))
    minute.append(int(l[1]))
for i in range(0,n-1):
    if hour[i]==hour[i+1] and minute[i]==minute[i+1]:
      server+=1
print(server)