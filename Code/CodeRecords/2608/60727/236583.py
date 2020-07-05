li=['a','e','i','o','u']
num = int(input())

for m in range(0,num):
    flag = 0
    data = input()
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            if data[i] in li and data[j] not in li:
                print(data[i:j+1])
                print('')
                flag=1
               
    if flag==0:
        print(-1)
        