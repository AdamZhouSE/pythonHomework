def find(string1,string2):
    result = []
    for m in string1:
        if(m in string2):
            result.append(m)
    print(" ".join(result))

n = input()
string1 = "".join(input().split(" "))
string2 = "".join(input().split(" "))
find(string1,string2)