i = [int(x) for x in input()[:-1].split("+")]
j = [int(x) for x in input()[:-1].split("+")]
print("{}+{}i".format(i[0]*j[0]-i[1]*j[1],i[1]*j[0]+i[0]*j[1]))