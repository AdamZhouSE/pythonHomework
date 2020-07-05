def move(num,char):
    all = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return all[(all.index(char)+num)%26]


num = int(input())
string = input()
res = ""
for i in string:
    res = res + move(num,i)
print(res,end="")