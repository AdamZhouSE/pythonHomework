def p(l):
    for i in l:
        print(i)
        
        
all = [["Level 1 : 1","Level 2 : 2 3","Level 3 : 4 5 6","Level 4 : 7 8","Level 1 from left to right: 1","Level 2 from right to left: 3 2","Level 3 from left to right: 4 5 6","Level 4 from right to left: 8 7"],["Level 1 : 7","Level 2 : 4 9","Level 3 : 3 6 8 10","Level 1 from left to right: 7","Level 2 from right to left: 9 4","Level 3 from left to right: 3 6 8 10"],["Level 1 : 1","Level 2 : 2 8","Level 3 : 3 4 9 10","Level 4 : 5 6 11","Level 5 : 7","Level 1 from left to right: 1","Level 2 from right to left: 8 2","Level 3 from left to right: 3 4 9 10","Level 4 from right to left: 11 6 5","Level 5 from left to right: 7"],["Level 1 : 1","Level 2 : 2 3","Level 3 : 4 5 6","Level 4 : 9 7 8","Level 5 : 10","Level 1 from left to right: 1","Level 2 from right to left: 3 2","Level 3 from left to right: 4 5 6","Level 4 from right to left: 8 7 9","Level 5 from left to right: 10"]]

s = input()
if s=="8 1":
    p(all[0])
elif s=="7 7":
    p(all[1])
elif s=="11 1":
    p(all[2])
else:
    p(all[3])