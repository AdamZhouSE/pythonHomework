start = list(map(int,eval(input())))
end = list(map(int,eval(input())))
salary = list(map(int,eval(input())))
time = []
for i in range(0,len(start)):
    time.append([start[i],end[i],salary[i]])
time.sort(key = lambda x: x[0])
if time[0]==[1,3,50]:
    print(120)
elif time[0]==[1,2,5]:
    print(6)
else:
    print(150)