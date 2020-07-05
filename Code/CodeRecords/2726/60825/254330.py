aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")


for i in range(len(l)):
    if l[i]=='null':
        deep=1
        begin=0
        while i>begin:
            deep+=1
            begin=begin*2+1
        print(deep-1)
        break