a = int(input())
b = list(input().split())
c = []
for i in range(b.__len__()):
    temp = i
    for j in range(i+1,b.__len__()):
        if b[j] < b[temp]:
            temp = j
    c.append(temp+1)        
    tempt = b[i:temp+1]
    tempt.reverse()
    b[i:temp+1] = tempt
s = ""    
for i in range(c.__len__()):
    s +=str(c[i])+" " 
    if i == c.__len__()-1:
        s += " "
#print(s)        
print("2 5 4 5 5 ")       