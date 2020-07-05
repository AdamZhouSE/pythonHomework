num_array=input().split(",")
n=len(num_array)
temp=[]
for x in range(0,n+1):
    temp.append(x)
for h in temp:
    if not h in num_array:
        print(h)