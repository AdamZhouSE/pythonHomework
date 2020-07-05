arrin = eval(input())
for i in range(0,len(arrin),2):
    if i==len(arrin)-1:
        print(arrin[i])
        break
    elif arrin[i]!=arrin[i+1]:
        print(arrin[i])
        break
