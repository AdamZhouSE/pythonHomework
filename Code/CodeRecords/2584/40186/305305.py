def Nim(m):
    if m==1 or m==2 or m==3:
        return 'True'
    elif Nim(m-1)=='False' or Nim(m-2)=='False' or Nim(m-3)=='False':
        return 'True'
    else:
        return 'False'

inp = int(input())
res = Nim(inp)
print(res)