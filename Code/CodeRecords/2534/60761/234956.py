k_list=input("")
result=[]
for letter in k_list:
    if('0'<=letter<='9'):
        result.append(int(letter))
result.sort()
print(result)
