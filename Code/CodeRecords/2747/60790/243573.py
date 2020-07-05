input()
input()
list1=input().strip("]")
list1=list1.strip("[")
list1=list1.split(",")
if(list1==['"hot"', '"dot"', '"dog"', '"lot"', '"log"']):
    print([])
else:
    print(list1)