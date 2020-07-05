i_j=input("").split(" ")
i=int(i_j[0])
j=int(i_j[1])
list_i=input("").split(" ")
list_j=input("").split(" ")
i_odd=0
i_even=0
j_odd=0
j_even=0
for a in range(i):
    if(int(list_i[a])%2==0):
        i_even=i_even+1
    else:
        i_odd=i_odd+1
for a in range(j):
    if(int(list_j[a])%2==0):
        j_even=j_even+1
    else:
        j_odd=j_odd+1
sum=min(i_even,j_odd)+min(i_odd,j_even)
print(sum)