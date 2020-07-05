str0 = input()
if str0[len(str0)-2:len(str0)] == "IV" : str0 = str0[0:len(str0)-2]+"Q"
if str0[len(str0)-2:len(str0)] == "IX" : str0 = str0[0:len(str0)-2]+"W"
if str0[len(str0)-2:len(str0)] == "XL" : str0 = str0[0:len(str0)-2]+"E"
if str0[len(str0)-2:len(str0)] == "XC" : str0 = str0[0:len(str0)-2]+"R"
if str0[len(str0)-2:len(str0)] == "CD" : str0 = str0[0:len(str0)-2]+"T"
if str0[len(str0)-2:len(str0)] == "CM" : str0 = str0[0:len(str0)-2]+"Y"
if str0.find("IV")!=-1:str0 = str0[0:str0.find("IV")]+"Q"+str0[str0.find("IV")+2:]
if str0.find("IX")!=-1:str0 = str0[0:str0.find("IX")]+"W"+str0[str0.find("IX")+2:]
if str0.find("XL")!=-1:str0 = str0[0:str0.find("XL")]+"E"+str0[str0.find("XL")+2:]
if str0.find("XC")!=-1:str0 = str0[0:str0.find("XC")]+"R"+str0[str0.find("XC")+2:]
if str0.find("CD")!=-1:str0 = str0[0:str0.find("CD")]+"T"+str0[str0.find("CD")+2:]
if str0.find("CM")!=-1:str0 = str0[0:str0.find("CM")]+"Y"+str0[str0.find("CM")+2:]
num = 0
for x in str0:
    if x == "I": num += 1
    elif x == "V": num += 5
    elif x == "X": num += 10
    elif x == "L": num += 50
    elif x == "C": num += 100
    elif x == "D": num += 500
    elif x == "M": num += 1000
    elif x == "Q": num += 4
    elif x == "W": num += 9
    elif x == "E": num += 40
    elif x == "R": num += 90
    elif x == "T": num += 400
    elif x == "Y": num += 900
print(num)

