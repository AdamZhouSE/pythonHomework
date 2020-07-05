temp = input().split(" ")
m, n = int(temp[0]), int(temp[1])
for i in range(m):
    temp=input()
    if temp.count("B")!=0:
        print(str(i+1+temp.count("B")//2)+" "+str(temp.index("B")+1+temp.count("B")//2))
        break
