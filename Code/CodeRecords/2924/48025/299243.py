n, r, avg = list(map(int, input().split()))
ab_list = []
for i in range(0, n):
    a, b = list(map(int, input().split()))
    ab_list.append([a,b])

total_needed = avg * n
vanya_total = 0
for i in range(0, n):
    vanya_total += ab_list[i][0]
diff = total_needed - vanya_total
#print(diff)
result = 0
ab_list = sorted(ab_list, key=lambda x: (x[1]))
#print(ab_list)
if (diff <= 0):
    print(0)
else:
    counter = 0
    while (diff > 0):
        if (ab_list[counter][0] >= r):
            #print('第',i,'項無法加分了')
            counter += 1
        else:

            result += ab_list[counter][1]
            diff -= 1
            ab_list[counter][0]+=1
            #print('第',i,'項加一分,diff=',diff)
    print(result)