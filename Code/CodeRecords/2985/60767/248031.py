def getString(num):
    if(num==1):
        return "A"
    else:
        return getString(num-1)+chr(64+(num))+getString(num-1)

num = int(input())
print(getString(num))