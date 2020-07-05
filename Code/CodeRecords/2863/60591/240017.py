string = input().split(" ")
high = eval(string[1])
count = 0
people = list(map(int,input().split(" ")))
for temp in people:
    if(temp > high):
        count += 2
    else:
        count += 1
print(count)