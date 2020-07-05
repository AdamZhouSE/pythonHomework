#当两个端点值相同时，返回该值即可；两个端点值不同时，最后一位必然不同。根据这一点来解题。
def bitAnd(a,b):
    if a==b:
        return a
    else:
        return bitAnd(int(a/2),int(b/2))<<1
list1=input("")
print(bitAnd(list1[0],list1[1]))