list=input().split(',')
for i in range(len(list)+1):
    if str(i) not in list:
        print(i)