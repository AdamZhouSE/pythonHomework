import collections, operator
temp = input()
temp = temp.split(" ")
s = temp[2][1:len(temp[2])-2]
t = temp[5][1:len(temp[5])-1]
dic1 = collections.Counter(s)
dic2 = collections.Counter(t)
if operator.eq(dic1,dic2):
    print("true")
else:
    print("false")