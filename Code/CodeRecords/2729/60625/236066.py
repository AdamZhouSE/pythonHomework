string =input()
string=string[1:len(string)-1]
list1=string.split(",")
court=0
while court<len(list1)-1:
    if list1[court] != list1[court+1]:
        print(list1[court])
        break
    court=court+2