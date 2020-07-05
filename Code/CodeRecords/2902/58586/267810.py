lines=int(input())
cry=-1
for i in range(lines//2+1):
    cry+=2
    star=(lines-cry)//2
    print("*"*star+"D"*cry+"*"*star)
for i in range(lines//2+1,lines):
    cry-=2
    star=(lines-cry)//2
    print("*"*star+"D"*cry+"*"*star)