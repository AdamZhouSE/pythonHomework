a = [int(i) for i in input().replace("[","").replace("]","").replace(",","").split(" ")]
result = 1
for i in a:
    if a.count(i-1)==0:
        length = 1
        while a.count(i+length) !=0:
            length+=1
        result = max(result,length)
print(result)