size=int(input())
list1=list(input())
count=0
def level_to_score(level):
    levels = {
        'A' : 4,
        'B': 3,
        'C' : 2,
        'D': 1,
        'E':0,
        'F': 0
    }
    return levels.get(level, None)


for i in range(size):
    count+=level_to_score(list1[i])
count=count/size
if count==0:
    print(0,end='')
else:
    print("%.14f" %count,end='')