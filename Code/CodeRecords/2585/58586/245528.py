line1=input()
line2=input()
start=[c for c in line1]
end=[c for c in line2]
flag=True
i=0
while i<len(start):
    if start[i]==end[i]:
        i+=1
        continue
    else:
        if i==len(start)-1:
            flag=False
            break
        else:
            if start[i:i+2]==["X","L"] and end[i:i+2]==["L","X"]:
                temp=start[i]
                start[i]=start[i+1]
                start[i+1]=temp
                i+=1
            elif start[i:i+2]==["R","X"] and end[i:i+2]==["X","R"]:
                temp = start[i]
                start[i] = start[i + 1]
                start[i + 1] = temp
                i+=1
            else:
                flag=False
                break
print(flag)