inp = eval(input())
#print(inp)
length = int(len(inp)/3)

result = []
cm =0
cn =0
m=n=inp[0]
#print(m)
for i in range(len(inp)):
    if(cm == 0 or m==inp[i]):
        cm = cm+1 
        m = inp[i]
    elif(cn == 0 or n == inp[i]):
        cn = cn + 1
        n = inp[i]
    else:
        cm = 0
        cn = 0
    
    if(cm>length):
        try:
            result.index(m)
        except:
            result.append(m)
    if(cn >length):
        try:
            result.index(n)
        except:
            result.append(n)
print(result)
