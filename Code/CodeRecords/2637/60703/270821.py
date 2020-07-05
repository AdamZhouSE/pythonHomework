listt = eval(input())
temp = listt
listt.sort(reverse = True)
res  = temp.index(listt[0])
if(res==0):print(1)
else:
    print(temp.index(listt[0]))