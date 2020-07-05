list=input();
for i in range(0,len(list)):
   if list[i-1]!=list[i]:
    if list[i]!=list[i+1]:
         print(list[i]);