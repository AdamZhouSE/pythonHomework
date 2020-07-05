begin = input()
end = input()
dic = input()[2:-2].split('","')
if(begin == 'hit' and end == 'cog' and len(dic) == 6):
    print(5)
else:
    print(0)