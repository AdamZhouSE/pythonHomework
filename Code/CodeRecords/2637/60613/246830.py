string=input()
num=list(map(int,string[1:len(string)-1].split(",")))
print(num.index(max(num)))