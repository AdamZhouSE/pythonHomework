string = input()
suffixs = []
for i in range(len(string)):
    suffixs.append([i+1,string[i:]])
suffixs = sorted(suffixs,key = lambda x:x[1])
index = []
for i,v in suffixs:
    print(i,end = ' ')