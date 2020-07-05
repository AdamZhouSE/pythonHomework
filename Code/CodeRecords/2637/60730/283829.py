m = eval(input())
for i in range(len(m)):
            if m[i] > m[i+1]:
                print(i)
                exit()