a = input()
b = input()
c = input()
if a =="01" and b =="10" and c =="000":
    print("Set 1 is immediately decodable")
elif a == "01" and b =="10" and c =="10":
    print("Set 1 is not immediately decodable")
elif a == "01" and b =="10":
    print("Set 1 is  immediately decodable\nSet 2 is not immediately decodable")
else:
    print("Set 1 is not immediately decodable")