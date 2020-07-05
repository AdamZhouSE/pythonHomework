num = int(input())
str1 = input().split(' ')
lists =[int(i) for i in str1]
lists.sort()
index = min(lists)
need = 0
#print(lists)
for i in range(1,num):
    if lists[i]>index:
#        print("OK")
        index = lists[i]
        continue
    else:
        temp = lists[i]
        lists[i]=index+1
        index += 1
 #       print("need:{}and{}".format(lists[i]-temp,i))
        need += (lists[i]-temp)
print(need)